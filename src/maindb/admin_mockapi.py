from helpers.director.shortcut import TablePage,ModelTable,ModelFields,director,page_dc,director_view,get_request_cache
from .models import MockApi
import json
from django.http import Http404,JsonResponse

class MockapiPage(TablePage):
    def get_label(self):
        return '虚拟API管理'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = MockApi
        exclude =[]
        pop_edit_fields=['id']

class MockapiForm(ModelFields):
    class Meta:
        model = MockApi
        exclude =[]
    
    #def after_save(self):
        #director.update({
            #self.instance.url:dyn_mock_api
        #})


@director_view('mock')
def dyn_mock_api(api):
    #request = get_request_cache()['request']
    #path = request.get_full_path()
    #direcor_name = path[5:]
    try:
        mock = MockApi.objects.get(url=api)

        return JsonResponse( json.loads(mock.content,encoding=False) )
    except MockApi.DoesNotExist:
        return JsonResponse({'msg':"api找不到"}) 

dc ={}
for inst in MockApi.objects.all():
    dc[inst.url] = dyn_mock_api

director.update(dc)

director.update({
    'mockapi':MockapiPage.tableCls,
    'mockapi.edit': MockapiForm,
})
page_dc.update({
    'mockapi':MockapiPage
})
