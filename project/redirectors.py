from django.http import HttpResponse, HttpResponseRedirect

def tv_channel_schedule(request, key):
    return HttpResponseRedirect("http://tv.azpm.org/schedules/%s/" % key)
    
def tv_episode_detail(request, id):
    return HttpResponseRedirect("http://tv.azpm.org/schedules/episode/%d/" % int(id))