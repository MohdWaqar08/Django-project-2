from .models import Subreddits

def global_subreddits(request):
    subreddits = Subreddits.objects.all().order_by('name')
    return {
        'sidebar_subreddits':subreddits
    }

