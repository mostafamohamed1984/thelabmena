import facebook
from django.conf import settings

def check_facebook_updates():
    try:
        # Initialize Facebook Graph API
        graph = facebook.GraphAPI(access_token=settings.FACEBOOK_ACCESS_TOKEN)
        
        # Get posts from your page
        posts = graph.get_object(
            id='61564050178957/posts',  # Your Facebook page ID
            fields='message,created_time,permalink_url'
        )
        
        # Format the latest post
        if 'data' in posts and posts['data']:
            latest_post = posts['data'][0]
            return {
                'message': latest_post.get('message', ''),
                'link': latest_post.get('permalink_url', ''),
                'created_time': latest_post.get('created_time', '')
            }
        return None
    except Exception as e:
        print(f"Facebook API error: {e}")
        return None 