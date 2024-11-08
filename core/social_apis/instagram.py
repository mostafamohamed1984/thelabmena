from instagram_private_api import Client
from django.conf import settings

def check_instagram_updates():
    try:
        # Initialize Instagram API
        api = Client(
            username=settings.INSTAGRAM_USERNAME,
            password=settings.INSTAGRAM_PASSWORD
        )
        
        # Get user feed
        user_feed = api.user_feed(settings.INSTAGRAM_USER_ID)
        
        # Get latest post
        if user_feed['items']:
            latest_post = user_feed['items'][0]
            return {
                'caption': latest_post.get('caption', {}).get('text', ''),
                'link': f"https://instagram.com/p/{latest_post['code']}",
                'timestamp': latest_post.get('taken_at', '')
            }
        return None
    except Exception as e:
        print(f"Instagram API error: {e}")
        return None 