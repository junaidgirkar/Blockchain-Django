import imp
import re
from django.shortcuts import render
from .models import Block, JGChain
import hashlib, json
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.
def home_view(request):
    
    # render function takes argument - request
    # and return HTML as response
    return render(request, "home.html")

def verify_blockchain():
    chain = Block.objects.all().order_by('-id')
    for i in range(1, len(chain)):
        if(chain[i].previous_hash != chain[i-1].current_hash):
            return False, i+1
    return True, 0

def get_chain(request):
    chain = Block.objects.all().order_by('-id')
    secure, tampered_block_id = verify_blockchain()
    return render(request, "get_chain.html", {'chain': chain, 'secure': secure, 'tampered_block_id': tampered_block_id})



# generate a hash of an entire block
def hash(block):
    # assuming obj is your model instance
    json_data = model_to_dict(block)
    print(json_data)
    if 'current_hash' in json_data: 
        del json_data['current_hash']
    print(json_data)
    encoded_block = json.dumps(json_data, sort_keys=True).encode()
    second_encoded_block = hashlib.sha256(encoded_block).hexdigest().encode()

    return hashlib.sha256(second_encoded_block).hexdigest()

def get_latest_block():
    return Block.objects.all().order_by('-id')[0]

@csrf_exempt
def mine_block(request):
    if(request.method == 'GET'):
        return render(request, "mine_block.html")

    # get the data we need to create a block
    if(request.method == 'POST'):

        # GENESIS BLOCK
        if(len(Block.objects.all()) == 0):
            previous_hash = '0000000000000000000000000000000000000000000000000000000000000000'
            data = request.POST.get('data')
            nonce = request.POST.get('nonce')
            new_block = Block.objects.create(previous_hash=previous_hash, data=data, nonce=nonce)
            current_hash = hash(new_block)
            new_block.current_hash = current_hash
            new_block.save()
            return render(request, "mine_block.html", {'MinedBlock': new_block})
        
        else:
            previous_block = get_latest_block()
            previous_hash = previous_block.current_hash
            data = request.POST.get('data')
            nonce = request.POST.get('nonce')
            new_block = Block.objects.create(previous_hash=previous_hash, data=data, nonce=nonce)
            current_hash = hash(new_block)
            new_block.current_hash = current_hash
            new_block.save()
            return render(request, "mine_block.html", {'MinedBlock': new_block})


def block_detail_view(request, id):
    block = Block.objects.get(id=id)
    return render(request, "block_detail.html", {'detail_block': block})


def attack_a_block(request):
    if(request.method == 'GET'):
        return render(request, "attack_a_block.html")

    elif(request.method == 'POST'):
        block_id = request.POST.get('block_id')
        block = Block.objects.get(id=block_id)
        block.data = request.POST.get('MaliciousData')
        block.save()
        current_hash = hash(block)
        block.current_hash = current_hash
        block.save()

        return render(request, "attack_a_block.html", {'AttackedBlock': block})