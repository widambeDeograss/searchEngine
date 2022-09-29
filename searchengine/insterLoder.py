import instaloader as IL
from instagramy import InstagramUser as IU
from instagramy import InstagramHashTag
import time

class InsterLoder:
    def __init__(self):
        self.loader = IL.Instaloader()
        # self.loader.login('gijjahjr', 'Jae@230679')
        # self.loader.interactive_login('gijjahjr')
        # self.loader.load_session_from_file('gijjahjr')
        # self.loader.interactive_login(username)


    def profiler_username(self, username):
        # User profile class to access metadata of account
        profile = IL.Profile.from_username(self.loader.context, username)
        # print(profile.get_posts())
        followers = []
        user_followers = profile.get_followers()
        for follower in user_followers:
            followers.append(follower)

        # returns iterator to list of followees
        # (followings) of given profile
        followees = []
        for followee in profile.get_followees():
            followees.append(followee)

        number_of_posts = profile.mediacount
        video_posts = profile.igtvcount
        bio = profile.biography
        profile_pic = profile.profile_pic_url
        business = profile.is_business_account

        posts = []
        postlikes = []
        postcomments = []
        for post in profile.get_posts():
            posts.append(post.url)
            post_likes = post.get_likes()
            post_commemts = post.get_comments()
            print(post_likes)
            print(post_commemts)
            postlikes.append(post_likes)
            postcomments.append(post_commemts)
            self.loader.download_post(post, username)


            # Iterate over all likes of the post. A profile instance of each likee is yielded.
            for likee in post_likes:
                print(likee.username)

            # Iterate over all comments of the post.
            # Each comment is representated by a PostComment namedtuple with fields.
            # text (string), created_at (datetime), id(int), owner(Profile)
            # and answers (~typing. Iterator[PostCommentAnswer]) is available.
            for comment in post_commemts:
                print(comment.owner.username)

    def profiler_hashtag(self, hashtag):
        posts = IL.Hashtag.from_name(self.loader.context, hashtag).get_posts()

        hasgtagposts = []

        for post in posts:
            hasgtagposts.append(post.url)
            print(post)

            self.loader.download_post(post, hashtag)



class Instagramy:
    def __init__(self, username):
        time.sleep(5)
        self.username = username
        self.unInstance = IU(self.username)

    def get_hashtag(self, hashtag):
        time.sleep(5)
        hashisntance = InstagramHashTag(hashtag)

        hashtagpostNO = hashisntance.number_of_posts

        hashtagjson =  hashisntance.get_json()
        print(hashtagpostNO)
        print(hashtagjson)

    def get_user(self):
        time.sleep(5)
        # getting total number of followings
        followingNo = self.unInstance.number_of_followings

        # getting total number of followers
        followersNo = self.unInstance.number_of_followers


        # getting total number of posts made inc(short vids, long vids and pictures)
        postsNo = self.unInstance.number_of_posts
        print(postsNo)

        # getting description of the account's bio
        instaBioDesc = self.unInstance.biography

        # getting links present in the account's bio
        instaBioLinks = self.unInstance.website

        # get a/c verification status
        verified = self.unInstance.is_verified
        print(verified)

        istadata =  {
            'is user verified': verified,
            'no of followers':followingNo,
            'no of following':followersNo,
            'no of posts': postsNo,
            'description of the bio':instaBioDesc,
            'biolinks': instaBioLinks
        }
        print(istadata)
        # return istadata
        return self.username.json



# # Get username from instagrame account
# username = input("Enter valid account username: ")
# obj =  InsterLoder(username)
# obj.profiler()




# enter valid instagram username
givenUN = input("Enter valid Instagram's username: ")
obj = Instagramy(givenUN)
obj.get_user()
obj.get_hashtag('sensabika')





