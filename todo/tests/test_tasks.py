from rest_framework import status
from users.models import Customuser
from todo.models import Todo
import pytest 
from model_bakery import baker

@pytest.mark.django_db
class TestCreateTask:
    def test_if_user_anonymous_return_401(self,api_client):

        response = api_client.post('/api/tasks/',{'title':'a',
                                                 'description':'aa'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_authenticated_return_201(slef,api_client,authenticate):
        user = Customuser.objects.create_user(username='test',password='test')
        api_client.force_authenticate(user=user)
    
        response = api_client.post('/api/tasks/',{'title':'a',
                                                 'description':'aa'})
        
        assert response.status_code == status.HTTP_201_CREATED 

    def test_if_user_authenticated_invalid_data_return_400(self,api_client):
        user = Customuser.objects.create_user(username='test',password='test')
        api_client.force_authenticate(user=user)
    
        response = api_client.post('/api/tasks/',{'title':'',
                                                 'description':'aa'})
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestRetriveTasks:
    
    def test_if_user_anonymous_return_401(self,api_client):

        response = api_client.get('/api/tasks/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_authenticated_return_200(self,api_client):
        user = Customuser.objects.create_user(username='test',password='test')
        task = Todo.objects.create(user_id=user.id,title='a',description='aa')
        api_client.force_authenticate(user=user)
    
        response = api_client.get('/api/tasks/')
        
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_anonmyous_get_one_task_retuen_401(self,api_client,authenticate):
        user = Customuser.objects.create_user(username='test',password='test')
        task = Todo.objects.create(user_id=user.id,title='a',description='aa')

        response = api_client.get(f'/api/tasks/{task.id}/',)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_authenticated_get_one_task_retuen_200(self,api_client,authenticate):
        user = Customuser.objects.create_user(username='test',password='test')
        task = Todo.objects.create(user_id=user.id,title='a',description='aa')
        
        api_client.force_authenticate(user=user)
        
    
        response = api_client.get(f'/api/tasks/{task.id}/')
        
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestDeleteTasks:
    def test_if_user_authenticated_delete_task_retuen_204(self,api_client,authenticate):
        user = Customuser.objects.create_user(username='test',password='test')
        task = Todo.objects.create(user_id=user.id,title='a',description='aa')
        
        api_client.force_authenticate(user=user)
        
    
        response = api_client.delete(f'/api/tasks/{task.id}/')
        
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_anonymous_user_delete_task_retuen_401(self,api_client,authenticate):
        user = Customuser.objects.create_user(username='test',password='test')
        task = Todo.objects.create(user_id=user.id,title='a',description='aa')
    
        response = api_client.delete(f'/api/tasks/{task.id}/')
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestUpdateTasks:
    def test_if_anonymous_user_update_task_retuen_401(self,api_client,authenticate):
        user = Customuser.objects.create_user(username='test',password='test')
        task = Todo.objects.create(user_id=user.id,title='a',description='aa')
    
        response = api_client.put(f'/api/tasks/{task.id}/',{'title':'aaaa'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_authenticated_user_update_task_retuen_200(self,api_client,authenticate):
        user = Customuser.objects.create_user(username='test',password='test')
        task = Todo.objects.create(user_id=user.id,title='a',description='aa')

        api_client.force_authenticate(user=user)
    
        response = api_client.put(f'/api/tasks/{task.id}/',{'title':'aaaa'})
        
        assert response.status_code == status.HTTP_200_OK 

    def test_if_authenticated_user_update_task_invalid_data_retuen_400(self,api_client,authenticate):
        user = Customuser.objects.create_user(username='test',password='test')
        task = Todo.objects.create(user_id=user.id,title='a',description='aa')

        api_client.force_authenticate(user=user)
    
        response = api_client.put(f'/api/tasks/{task.id}/',{'title':''})
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST   





        
