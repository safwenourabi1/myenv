from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import ticket
from accounts.models import accounts
from accounts.views import var
from django.views.generic import DeleteView
from django.urls import reverse_lazy
# Create your views here.


def main(request):
   
    cu = request.user
    print(cu.id)
    if cu.id==None:
         return redirect('loginuser')
             
    user=""
    objects=[]
    if cu.is_superuser==False:
        for elem in ticket.objects.all() :
            if cu.id == elem.created_by_id :
                  
                  objects.append((elem,cu.username))
      
    else:
        tickets = [elem for elem in ticket.objects.all()  ] 
        print(tickets)
      
        for elem in tickets :
            for elem2 in User.objects.all():
                if elem2.id == elem.created_by_id :
                    objects.append((elem,elem2.username))
        print(objects)
        
    empty=True        
    if request.method == 'POST':
        title= request.POST['title']
        description= request.POST['message']

        ticket.objects.create(
            title=title,
            description=description,
            created_by=cu,
            )
        return redirect('/main')
    if len(objects)==0:
         empty=True
    else:
         empty=False     
    print("saaaaaaaaaaaaaaaamir",empty)

    return  render (request ,'page2.html', {'objects':objects,'cu':cu,'empty':empty},)



def deletepost(request,id):
        print(id)
        print('hello')
        item_to_delete = get_object_or_404(ticket, pk=id)
        print(item_to_delete.description)
        item_to_delete.delete()
        return redirect('main')
   
