# bilibilivideodownload2

#B站视频下载器	
#不再使用SESSDATA进行登录	
#改用cookies.sqlite进行登录，cookies.sqlite获取方法	
Firefox查看cookie 方法在地址栏输入 about:preferences#privacy ，或选择“选项”项 ->隐私与安全-> cookie和网站数据/管理数据...，也可以F12在开发人员窗口查看当前访问网站的cookie信息。windows下Firefox的cookie位置是“%APPDATA%\Roaming\Mozilla\Firefox\Profiles\ xxx.default\cookies.sqlite的文件”。 在Linux Firefox的Cookie路径为“$HOME/.mozilla/firefox/xxxx.default/cookie.sqlite”。	
#使用的是you-get库下载，直接写入硬盘	
#相比与第一个版本登录操作稍微复杂一点，以及下载视频要等you-get解析视频地址	
#好处是可以下载别的视频网站视频，不局限与B站，只要你的cookies.sqlite里面有该视频网站的cookie，理论上都能在最高清晰度的视频	
#需要配置ffmpeg环境变量	
#无ffmpeg会下载FLV文件，有ffmpeg会自动下载mp4源	
#可根据用户UID和页数进行用户的全部视频下载	
#想要自动获取页数的自己可以下代码去修改一下即可	
