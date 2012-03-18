# Create your views here.
from django.shortcuts import render_to_response
from cmdb.biz.SourceManager import QuerySourceManager

def queryInfoByIp2Web(request,ip):
    #ip = request.GET['ip']
    appBiz = QuerySourceManager().queryAppBizByIp(ip)
    appInstance = QuerySourceManager().queryAppInstanceByIp(ip)
    return render_to_response('query_result.html',{'appBiz':appBiz,'appInstance':appInstance})
    
    
#def queryInfoByIp2Service(request):
#    ip = request.GET.get('ip','')
#    appBiz = QuerySourceManager().queryAppBizByIp(ip)
#    appInstance = QuerySourceManager().queryAppInstanceByIp(ip)
#    return locals()
    
    