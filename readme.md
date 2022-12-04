# NeoForum
Форум для быстрого общения в интернете.
# API
1. /api/themes/ - возвращает JSON строку: \
**{"themes" : ["sport", "motosport", "programming", "offtop"]}** 
2. /api/threads_THEMENAME/ - возвращает  JSON строку, содержит все треды на тему THEMENAME:\
**{"threads" : [{"id" : "1", "creator_name" : "sample name", "thread_title" : "sample text", "thread_body" : "sample text", "pic" : "base64 pic code"}]}** 
3. /api/thread_THREADID/ - возвращает строку в формате JSON, содержит информацию о треде THREADID и о постах в треде THREADID:\
**{"creator_name" : "sample name", "thread_titile":"sample text", "posts" : [{"post_id" : "0", "date" : "01.12.2022", "time" : "13:41", "post_creator" : "sampla name", "post_text" : "sample text", "post_pic" : "base64 pic code"}]}**