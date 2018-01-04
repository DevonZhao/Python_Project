#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Note：json处理的应用实例
'''

json.dumps
json.loads

json.dumps():序列化数据类型为字符串
json.loads():反序列化成数据类型
json.loads()把Json格式字符串解码，转换成Python对象。
demjson

'''


import json
import demjson

share_data = {"feed":[{"uid":39997720,"title":"诚","text":"忠诚、诚信、真诚、坦诚、诚实、诚恳、实在，表面看起来意思大同小异，其实不然。用忠诚和诚恳对待自己工作，用努力换来公司的信任，是我的使命。有些人觉得，明明自己对公司做了很多贡献，换来的回报和付出却不成正比。有时候，我们可以扪心自问：真的做好了吗？俗话说得好，是金子总会发光。对于家庭，真诚地付出必不可少。这一点，我是内疚的：家人一直希望我多一些陪伴，尤其是那两岁的宝贝女儿。在过去的2017年，我有愧于他们，在即将到来的2018年，我会尽全力多一些陪伴和爱。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4930/8742_24_C1w9A1dRO7T8xC","turl":"http://i9.taou.com/maimai/p/4930/8742_24_C1w9A1dRO7T8xC-t480","y":900,"x":750}],"uinfo":{"province":"广东","major":17,"py":"guo1郭fei1飞","dist":0,"figure":33497053,"cmf2":"","is_prof":"false","cmf1":"","profession":2,"rank":76,"line2":"","local_mobile":"","mem_id":2,"id":39997720,"loc":"广东","ouid":269686428,"mmid":"39997720","utype":1,"cmf_no6":0,"line4":"通信电子 | 行政人事, 影响力: 76","line3":"三星执行副总(广东)","compos":"三星执行副总","line1":"三星执行副总","in_app":1,"lv":0,"is_co":"false","tid":"m4oQUWHn7W","mem_st":0,"status":1,"is_hp":"false","city":"深圳","company":"三星","short_compos":"三星执行副总","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozOTk5NzcyMCwibGV2ZWwiOjAsInQiOiJjdHQifQ.cpET_7HFqvF7tZINmX32Q1RCu-EBn_uLc5HoGEB9AWI","judge":1,"is_sh":"false","qp":2.630000114440918,"name":"郭飞","career":"三星执行副总","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/3349/7053_24_I8s6Xam1V6W1zV-a160","is_exco":"false","cmf":0,"position":"执行副总","job_line":"","short_career":"三星执行副总"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4930/8744_24_O23sWNdjA2MGb8","likes":845,"id":227652892,"crtime":"2017-12-20 10:17:23","pic_infos":"49308742,750,900"},{"uid":31601982,"title":"择","text":"90后到这个时候应该是最迷茫的时候，不上不下，就业迷茫，创业不敢，我也不例外。2017年，有很多想法，却没经验，没资本，没项目，从年初想到年底，跳了槽，离了职，再到待业，于是做了一个潜伏在心底已久的选择：创业。谁的青春不迷茫，但是，趁着年轻，还有资本，敢闯、敢拼、敢于尝试，就算失败，至少，我敢在那些敢想不敢做的人面前骄傲地说，我做了。希望在2018年，不管遇到什么困难，这个团队继续坚持下去，咬咬牙，都能挺过去！","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4930/8262_62_o4rqQ9QPMDLP97","turl":"http://i9.taou.com/maimai/p/4930/8262_62_o4rqQ9QPMDLP97-t480","y":900,"x":750}],"uinfo":{"province":"广东","major":30,"py":"zhang1张hang2航","dist":0,"figure":42107304,"cmf2":"","is_prof":"false","cmf1":"","profession":10,"rank":94,"line2":"","local_mobile":"","mem_id":2,"id":31601982,"loc":"广东","ouid":537859517,"mmid":"31601982","utype":1,"cmf_no6":0,"line4":"服务业 | 经营管理, 影响力: 94","line3":"阿木木科技有限公司联合创始人(广东)","compos":"阿木木科技有限公司联合创始人","line1":"阿木木科技有限公司联合创始人","in_app":1,"lv":0,"is_co":"false","tid":"m2ueEfqJ9mJ","mem_st":0,"status":1,"is_hp":"false","city":"广州","company":"阿木木科技有限公司","short_compos":"阿木木科技有限公司联合创始人","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozMTYwMTk4MiwibGV2ZWwiOjAsInQiOiJjdHQifQ.wiwmkGrgZ7za_P2BsERyYcQN4XrMqRl2skhbE52aQhQ","judge":0,"is_sh":"false","qp":2.200000047683716,"name":"张航","career":"阿木木科技有限公司联合创始人","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/4210/7304_62_C1hoUbtBhLhbhk-a160","is_exco":"false","cmf":0,"position":"联合创始人","job_line":"","short_career":"阿木木科技有限公司联合创始人"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4930/8265_62_F1KJSNQHrjAg7C","likes":782,"id":227651165,"crtime":"2017-12-20 10:14:51","pic_infos":"49308262,750,900"},{"uid":627494,"title":"炼","text":"这是在16年底CDX年会的主题，也是2017年乃至以后每一年的核心思想：永远把修炼当做最重要的事情。每一年，都有新的挑战，有喜悦有委屈，就像程维说的一句话，当你感觉到委屈的时候，你在进步。2017年，我们团队迎来了更多元的发展，从国内到国际，从线上到更深入的线下。团队的设计师开始满世界跑，调研各种国家的用户习惯，需求痛点，文化差异。从线上的用户体验，转向线上线下的服务设计，让设计师不只是在一张图、一张界面上用力，滴滴的设计师看到的是更加广泛的世界。2018年，会有更高的挑战等着我们跨越。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4930/5852_38_58GAkkhkw95hJO","turl":"http://i9.taou.com/maimai/p/4930/5852_38_58GAkkhkw95hJO-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":6,"py":"zhao4赵tian1天xiang2翔","dist":0,"figure":3837461,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":2594,"line2":"","local_mobile":"","mem_id":2,"id":627494,"loc":"北京","ouid":3758114957,"mmid":"627494","utype":1,"cmf_no6":0,"line4":"IT互联网 | 设计, 影响力: 2594","line3":"滴滴CDX设计总监(北京)","compos":"滴滴CDX设计总监","line1":"滴滴CDX设计总监","in_app":1,"lv":0,"is_co":"false","tid":"m55eg8sS5al","mem_st":0,"status":1,"is_hp":"false","city":"北京","company":"滴滴","short_compos":"滴滴CDX设计总监","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1Ijo2Mjc0OTQsImxldmVsIjowLCJ0IjoiY3R0In0.S8L7_7bRpgXB8HE_CRBAPaxVfR0nmv2cBZqX4maBVLM","judge":1,"is_sh":"false","qp":2.700000047683716,"name":"赵天翔","career":"滴滴CDX设计总监","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/383/7461_38_51JJNSmSEEkFzB-a160","is_exco":"false","cmf":0,"position":"CDX设计总监","job_line":"","short_career":"滴滴CDX设计总监"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4930/5853_38_bLsD02hTpl2k3w","likes":674,"id":227641966,"crtime":"2017-12-20 10:00:46","pic_infos":"49305852,750,900"},{"uid":321553,"title":"新","text":"休完产假回归后全新的一年，迎来了各种全新的体验：工作和业务的重新出发，幸运的是遇到了志同道合又靠谱的团队小伙伴；作为职场妈妈，面对着繁忙工作和认真养娃的双重压力，幸运的是有能干又贴心的家人无条件支持和帮助。希望2018年，继续新挑战，继续update自己！","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4931/2899_17_zIIzMYTtbNoazE","turl":"http://i9.taou.com/maimai/p/4931/2899_17_zIIzMYTtbNoazE-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":5,"py":"wei2韦cui4粹ting2婷","dist":0,"figure":49183376,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":246,"line2":"","local_mobile":"","mem_id":2,"id":321553,"loc":"北京","ouid":1476404052,"mmid":"321553","utype":1,"mem_st":1,"line4":"IT互联网 | 运营/编辑, 影响力: 246","line3":"脉脉用户运营总监(北京)","compos":"脉脉用户运营总监","line1":"脉脉用户运营总监","in_app":1,"lv":0,"is_co":"false","tid":"w1670166522","status":1,"is_hp":"false","city":"海淀区","cmf_no6":0,"company":"脉脉","short_compos":"脉脉用户运营总监","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozMjE1NTMsImxldmVsIjowLCJ0IjoiY3R0In0.B_4KcKgAEkqspLEAIM2tb-KxBDLssIoMkQkaKICgvYU","judge":1,"is_sh":"false","qp":2.730609893798828,"name":"韦粹婷","career":"脉脉用户运营总监","gender":2,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/4918/3376_17_m2Hs23otapJ4pe-a160","is_exco":"false","cmf":0,"position":"用户运营总监","job_line":"","short_career":"脉脉用户运营总监"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4931/2903_17_1eGtu5vf3nr3F2","likes":629,"id":227667968,"crtime":"2017-12-20 10:40:09","pic_infos":"49312899,750,900"},{"uid":585776,"title":"长","text":"这一年，对我个人来说，在工作上，是成长了很多。从一月到四月，独立接手基础运营工作，负责审核和客服的所有工作安排统筹，招聘入职培训等等。带领团队稳定持续工作，虽然有瑕疵，好在没有出现大问题，这是比较可喜的。为了提升自己，今年和很多小伙伴交流学习，带着问题交流更能抓住重点，学习到了很多，感谢这些朋友们。自我反思与学习，碰到问题先学习，慢慢的就能找到解决办法，现在我更愿意跟人交流，听取意见，共同成长。2017年很开心有一群优秀的同事，很感谢帮助过我的朋友们。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4930/3914_48_f7xre7Un1tbrB6","turl":"http://i9.taou.com/maimai/p/4930/3914_48_f7xre7Un1tbrB6-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":5,"py":"huang2黄hui4惠","dist":0,"figure":49384541,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":1529,"line2":"","local_mobile":"","mem_id":2,"id":585776,"loc":"北京","ouid":1342194581,"mmid":"585776","utype":1,"mem_st":1,"line4":"IT互联网 | 运营/编辑, 影响力: 1529","line3":"脉脉运营(北京)","compos":"脉脉运营","line1":"脉脉运营","in_app":1,"lv":0,"is_co":"false","tid":"m1MPjOMeNCy","status":1,"is_hp":"false","city":"海淀区","cmf_no6":0,"company":"脉脉","short_compos":"脉脉运营","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1Ijo1ODU3NzYsImxldmVsIjowLCJ0IjoiY3R0In0.3JgBTLjNfkQNoG0yvucVLckS-Ggx4fefwZZGh9JaAa0","judge":1,"is_sh":"false","qp":2.0999999046325684,"name":"黄惠","career":"脉脉运营","gender":2,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/4938/4541_48_U2QpQ6XuXGQhD6-a160","is_exco":"false","cmf":0,"position":"运营","job_line":"","short_career":"脉脉运营"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4930/3916_48_r149ALTWNh4Ufb","likes":607,"id":227634337,"crtime":"2017-12-20 09:47:21","pic_infos":"49303914,750,900"},{"uid":3564755,"title":"给","text":"2017年，是我分享最多的一年。5月，我在深圳第二届 @Swift 开发者大会上分享了《学习 iOS 编译原理能做哪些有意思的事情》。6月，我在GMTC 全球移动技术大会上分享了《滴滴出行 iOS 端瘦身实践》。8月，我在 APMCon 2017中国应用性能管理大会上分享了《深入剖析 iOS 性能优化》。12月，我在上海举行的 GIAC 全球互联网架构大会上分享了《Swift 将 Web 代码转成60帧满帧原生应用的方案及实践》。2017年马上就要过去，期待在新的一年，能够做出更多的东西，给予更多。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4931/242_83_91lQuWkzY7v5dE","turl":"http://i9.taou.com/maimai/p/4931/242_83_91lQuWkzY7v5dE-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":0,"py":"dai4戴ming2铭","dist":0,"figure":2854960,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":1756,"line2":"","local_mobile":"","mem_id":2,"id":3564755,"loc":"北京","ouid":1208071986,"mmid":"3564755","utype":1,"cmf_no6":0,"line4":"IT互联网 | 研发, 影响力: 1756","line3":"滴滴技术专家(北京)","compos":"滴滴技术专家","line1":"滴滴技术专家","in_app":1,"lv":0,"is_co":"false","tid":"m3KGORxPyqm","mem_st":0,"status":1,"is_hp":"false","city":"东城区","company":"滴滴","short_compos":"滴滴技术专家","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozNTY0NzU1LCJsZXZlbCI6MCwidCI6ImN0dCJ9.5vgEmTDaITjk71HlhDFdS45ZlLVjkDx3_wuS4EDP41I","judge":1,"is_sh":"false","qp":2.300950050354004,"name":"戴铭","career":"滴滴技术专家","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/285/4960_83_51E9ksAQMjhkxA-a160","is_exco":"false","cmf":0,"position":"技术专家","job_line":"","short_career":"滴滴技术专家"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4931/246_83_w1qmcOkAwSgJvi","likes":590,"id":227659044,"crtime":"2017-12-20 10:25:30","pic_infos":"49310242,750,900"},{"uid":121476,"title":"丰","text":"三年前开始创业，经历了各种艰难和波折，也经历了自己和团队飞速的成长。2017，这一年收获颇丰，公司和产品继续上一个台阶，每一个人都从创业这件事上得到了丰富的收获。感恩团队和合作伙伴，感恩家人，感恩朋友","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4931/2096_4_44lxcsGl6ln9y","turl":"http://i9.taou.com/maimai/p/4931/2096_4_44lxcsGl6ln9y-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":14,"py":"li3李shuai4帅","dist":0,"figure":15640476,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":247,"line2":"","local_mobile":"","mem_id":0,"id":121476,"loc":"北京","ouid":4026534592,"mmid":"121476","utype":1,"cmf_no6":0,"line4":"IT互联网 | 高管, 影响力: 247","line3":"圈子账本创始人&CEO(北京)","compos":"圈子账本创始人&CEO","line1":"圈子账本创始人&CEO","in_app":1,"lv":0,"is_co":"false","tid":"w1842042487","mem_st":0,"status":1,"is_hp":"false","city":"朝阳区","company":"圈子账本","short_compos":"圈子账本创始人&CEO","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjoxMjE0NzYsImxldmVsIjowLCJ0IjoiY3R0In0.zKBS5BxB20PIMdfa-0xDwem0FqhZdDl70Qwjl7xI708","judge":1,"is_sh":"false","qp":2.250469923019409,"name":"李帅","career":"圈子账本创始人&CEO","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/1564/476_4_41QJCp9fwKP3Nn-a160","is_exco":"false","cmf":0,"position":"创始人&CEO","job_line":"","short_career":"圈子账本创始人&CEO"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4931/2101_4_sfUcJgcA65NkZg","likes":540,"id":227665333,"crtime":"2017-12-20 10:35:38","pic_infos":"49312096,750,900"},{"uid":1668726,"title":"变","text":"转眼365天即过。2017年，我以不变应万变，也积极拥抱变化。工作上，项目的更替叠加，方式思路变化了，积极热情的工作态度没有变，全力以赴的工作激情没有变；生活上新里程的开始，让我体会人生五味杂陈，从迷茫无助到勇于面对，再到积极改变。面对-接受-改变，不论是主动的还是被动的，都是一段难忘的心路历程。在变的同时，我能比去年多一些深思，在熟虑后能加速前进，这是一年里自己不小的收获。不论时间和世界怎么变，请张开双臂，微笑着面对，这仅有一次的人生。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4930/9289_118_j2Qh5U9MhpKYbh","turl":"http://i9.taou.com/maimai/p/4930/9289_118_j2Qh5U9MhpKYbh-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":9,"py":"yang2杨wei1薇","dist":0,"figure":22399385,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":602,"line2":"","local_mobile":"","mem_id":2,"id":1668726,"loc":"北京","ouid":1610665895,"mmid":"1668726","utype":1,"cmf_no6":0,"line4":"IT互联网 | 市场商务, 影响力: 602","line3":"美团点评商务合作总监(北京)","compos":"美团点评商务合作总监","line1":"美团点评商务合作总监","in_app":1,"lv":0,"is_co":"false","tid":"m4R3K5T0EtP","mem_st":0,"status":1,"is_hp":"false","city":"朝阳区","company":"美团点评","short_compos":"美团点评商务合作总监","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjoxNjY4NzI2LCJsZXZlbCI6MCwidCI6ImN0dCJ9.o0ZUD-GMrmweE98YkzQ8WU3Ae9dmOlAxYH9Do55WgX4","judge":1,"is_sh":"false","qp":1.899999976158142,"name":"杨薇","career":"美团点评商务合作总监","gender":2,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/2239/9385_118_R4Wah96s3KnBZw-a160","is_exco":"false","cmf":0,"position":"商务合作总监","job_line":"","short_career":"美团点评商务合作总监"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4930/9292_118_B1997081WIzv9q","likes":527,"id":227654852,"crtime":"2017-12-20 10:20:15","pic_infos":"49309289,750,900"},{"uid":38464476,"title":"真","text":"2017年是自己作为职场菜鸟的第一个完整的年头，作为记者我亲历了太多的新闻现场，看到过虚假，看到过茫然，看到过无奈和愤怒，但每一次我都选择用最真实的笔记下。我见证着公司从一二十人成长为百人，从彼此心照不宣到内耗不断，但改变的是环境，不变的是内心，对于每个同事，每一个摆放着自己都真诚相待，这也让我收获很多，接下来的一年我会继续真诚待人，在成为一个优秀的记者路上不断前进。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4934/103_92_71yfIGrQKLpoBM","turl":"http://i9.taou.com/maimai/p/4934/103_92_71yfIGrQKLpoBM-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":17,"py":"dong3董jie2洁","dist":0,"figure":24525037,"cmf2":"","is_prof":"false","cmf1":"","profession":1,"rank":62,"line2":"","local_mobile":"","mem_id":0,"id":38464476,"loc":"北京","ouid":806507338,"mmid":"38464476","utype":1,"cmf_no6":0,"line4":"文化传媒 | 编辑记者, 影响力: 62","line3":"品途商业评论编辑记者(北京)","compos":"品途商业评论编辑记者","line1":"品途商业评论编辑记者","in_app":1,"lv":0,"is_co":"false","tid":"m1hcaWqONs6","mem_st":0,"status":1,"is_hp":"false","city":"朝阳区","company":"品途商业评论","short_compos":"品途商业评论编辑记者","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozODQ2NDQ3NiwibGV2ZWwiOjAsInQiOiJjdHQifQ.i4S2YyhvtAHiR7ZXfeci1aiqOGzQo388_XNJF74P4TA","judge":1,"is_sh":"false","qp":1.2999999523162842,"name":"董洁","career":"品途商业评论编辑记者","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/2452/5037_92_w1kNSTfHFrhtFa-a160","is_exco":"false","cmf":0,"position":"编辑记者","job_line":"","short_career":"品途商业评论编辑记者"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4934/106_92_o8RwK9rXpQenzN","likes":525,"id":227824454,"crtime":"2017-12-20 13:21:56","pic_infos":"49340103,750,900"},{"uid":1539928,"title":"免","text":"2017年充满了巨大的变化，即将成为人父，也搬到了新家，工作方面也是从comfort zone里面跳了出来，进入创业公司体会身心的全方位历练。公司同事有有一句话说的很好，其实创业的过程就是一个提高免疫力的过程，开始的时候遇到一点风吹草动，你会感冒发烧，渐渐的，你能承受的压力等级在慢慢的提升，最后你到了百毒不侵的时候，那个时候你就一定可以成事儿了。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4932/6191_88_t1zNx7BaCltzdT","turl":"http://i9.taou.com/maimai/p/4932/6191_88_t1zNx7BaCltzdT-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":24,"py":"qin2秦pei2培gen1根","dist":0,"figure":13009422,"cmf2":"","is_prof":"false","cmf1":"","profession":3,"rank":244,"line2":"","local_mobile":"","mem_id":0,"id":1539928,"loc":"北京","ouid":268484590,"mmid":"1539928","utype":1,"cmf_no6":0,"line4":"金融 | 财税审计, 影响力: 244","line3":"费曼（北京）科技有限公司财务总监(北京)","compos":"费曼（北京）科技有限公司财务总监","line1":"费曼（北京）科技有限公司财务总监","in_app":1,"lv":0,"is_co":"false","tid":"m3WehDtdWFl","mem_st":0,"status":1,"is_hp":"false","city":"北京","company":"费曼（北京）科技有限公司","short_compos":"费曼（北京）科技有限公司财务总监","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjoxNTM5OTI4LCJsZXZlbCI6MCwidCI6ImN0dCJ9.TprRBDauSSnmpdVSYe8Rvv6dLJ5r031Bl6i3O8_dnW0","judge":1,"is_sh":"false","qp":2.0362699031829834,"name":"秦培根","career":"费曼（北京）科技有限公司财务总监","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/1300/9422_88_B1caF4dr9MynHR-a160","is_exco":"false","cmf":0,"position":"财务总监","job_line":"","short_career":"费曼（北京）科技有限公司财务总监"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4932/6194_88_KFSWztByh1ivbG","likes":524,"id":227741142,"crtime":"2017-12-20 11:50:57","pic_infos":"49326191,750,900"},{"uid":129168210,"title":"筑","text":"2016年，上善若水。把一个一盘散沙的队伍，含有有沙子、水泥、石子这些看似独立无用、且格格不入的东西，用水搅拌成了混凝土。实现了队伍稳定，停滞6年的天然气项目恢复建设，两个项目竣工。公司从集团十二家企业的倒数第一跃居第五。\n2017年，厚德载物。带领团队，挑战了不可能。已经被弃置多年的公司终于投产经营，公司“浴火重生”，单位和个人奖励纷至沓来，一年的荣誉超过公司五年的总和还要多，人力资源、队伍士气、管理水平、绩效考核等指标均跃居集团第一，团队筑梦沈阳。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4950/3004_82_c2HlZLalAaY5z6","turl":"http://i9.taou.com/maimai/p/4950/3004_82_c2HlZLalAaY5z6-t480","y":900,"x":750}],"uinfo":{"province":"辽宁","major":15,"py":"shao4邵bo2博","dist":0,"figure":40848893,"cmf2":"","is_prof":"false","cmf1":"","profession":18,"rank":66,"line2":"","local_mobile":"","mem_id":0,"id":129168210,"loc":"辽宁","ouid":1077777294,"mmid":"129168210","utype":1,"cmf_no6":0,"line4":"化工能源 | 经营管理, 影响力: 66","line3":"中石油沈阳燃气公司总经理(辽宁)","compos":"中石油沈阳燃气公司总经理","line1":"中石油沈阳燃气公司总经理","in_app":1,"lv":0,"is_co":"false","tid":"m1PIG1g23O3","mem_st":0,"status":1,"is_hp":"false","city":"沈阳","company":"中石油沈阳燃气公司","short_compos":"中石油沈阳燃气公司总经理","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjoxMjkxNjgyMTAsImxldmVsIjowLCJ0IjoiY3R0In0.yuctTwlrv_GvTBDrzEXjTl0OTiVW9HaCQ_i_ResR9Jg","judge":1,"is_sh":"false","qp":2.061650037765503,"name":"邵博","career":"中石油沈阳燃气公司总经理","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/4084/8893_82_6cUfFPCsZ5iXHG-a160","is_exco":"false","cmf":0,"position":"总经理","job_line":"","short_career":"中石油沈阳燃气公司总经理"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4950/3005_82_ictfFPast5UXTG","likes":514,"id":228392528,"crtime":"2017-12-21 05:30:56","pic_infos":"49503004,750,900"},{"uid":30675175,"title":"起","text":"从28岁到29岁，从创业失败到再起来，依然无所畏惧，依旧勇往直前。不忘初心方得始终，以梦为马不负韶华。继续学习，思考，总结，让自己变得更强好是解决焦虑的唯一解药。2018，未来，已来，我准备好迎接挑战了，你呢？","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4971/5421_103_3eIcMfuvS6LxBr","turl":"http://i9.taou.com/maimai/p/4971/5421_103_3eIcMfuvS6LxBr-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":9,"py":"deng4邓zhang3长hong2弘","dist":0,"figure":37079352,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":165,"line2":"","local_mobile":"","mem_id":2,"id":30675175,"loc":"北京","ouid":3893273747,"mmid":"30675175","utype":1,"mem_st":1,"line4":"IT互联网 | 市场商务, 影响力: 165","line3":"脉脉高级品牌经理(北京)","compos":"脉脉高级品牌经理","line1":"脉脉高级品牌经理","in_app":1,"lv":0,"is_co":"false","tid":"m58Ksw9gRk6","status":1,"is_hp":"false","city":"朝阳区","cmf_no6":0,"company":"脉脉","short_compos":"脉脉高级品牌经理","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozMDY3NTE3NSwibGV2ZWwiOjAsInQiOiJjdHQifQ.vjF-ksveJtEEavZUQmIaZA_Xy2e1LeVrm-dEbLpcDVg","judge":1,"is_sh":"false","qp":2.1700000762939453,"name":"邓长弘","career":"脉脉高级品牌经理","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/3707/9352_103_b5bgNqWaGk9CVl-a160","is_exco":"false","cmf":0,"position":"高级品牌经理","job_line":"","short_career":"脉脉高级品牌经理"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4971/5426_103_w1zKaOu5jKt5dt","likes":480,"id":229133383,"crtime":"2017-12-22 00:24:43","pic_infos":"49715421,750,900"},{"uid":1769067,"title":"拼","text":"救治病人争分夺秒，看着病人慢慢康复，自己拼的很值得。医生工作都是拿命拼来的，经常加班，累了就随便倒在一个地方睡觉。上半年因为工作压力导致身体出了问题，于是开始健身并取得了不错的效果。同事关系上也比去年更好，做人不能太闷。对自己未来的预期是：当一个好医生。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4930/5264_107_E3AMiV1RpkAebG","turl":"http://i9.taou.com/maimai/p/4930/5264_107_E3AMiV1RpkAebG-t480","y":900,"x":750}],"uinfo":{"province":"西藏","major":0,"py":"li3李yang2阳","dist":0,"figure":49185929,"cmf2":"","is_prof":"false","cmf1":"","profession":6,"rank":55,"line2":"","local_mobile":"","mem_id":0,"id":1769067,"loc":"西藏","ouid":2281755623,"mmid":"1769067","utype":1,"cmf_no6":0,"line4":"医疗生物 | 医生, 影响力: 55","line3":"凤城市中医院医生(西藏)","compos":"凤城市中医院医生","line1":"凤城市中医院医生","in_app":1,"lv":0,"is_co":"false","tid":"m2FQTTBCVHA","mem_st":0,"status":111,"is_hp":"false","city":"日喀则","company":"凤城市中医院","short_compos":"凤城市中医院医生","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjoxNzY5MDY3LCJsZXZlbCI6MCwidCI6ImN0dCJ9.PTf8sq8JhLTSEMBu8UlNqVK1-UzyK_9Qd6MHlRW0w9Y","judge":0,"is_sh":"false","qp":1.2999999523162842,"name":"李阳","career":"凤城市中医院医生","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/4918/5929_107_g18Y1g5hrOHg1d-a160","is_exco":"false","cmf":0,"position":"医生","job_line":"","short_career":"凤城市中医院医生"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4930/5266_107_Q17nEy1nbMsRPK","likes":455,"id":227639401,"crtime":"2017-12-20 09:56:26","pic_infos":"49305264,750,900"},{"uid":30667660,"title":"稳","text":"17年是我做BD的第二年，也是职业生涯的第三个年头。从事这个岗位对我来说，已经基本实现从入门到精(fang)通(qi)，接下来我面临的是是否要继续现在的角色，还是在18年，19年，甚者更远，另辟蹊径。这对我整个职业生涯发展有着长远的影响，需要我认真规划。总之，17年对我来说是稳扎稳打，平步发展的一年，希望18年有质的飞跃。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4931/4299_12_61xXEuGkM5yV7C","turl":"http://i9.taou.com/maimai/p/4931/4299_12_61xXEuGkM5yV7C-t480","y":900,"x":750}],"uinfo":{"province":"上海","major":14,"py":"jiang3蒋rui4锐","dist":0,"figure":28541915,"cmf2":"","is_prof":"false","cmf1":"","profession":3,"rank":177,"line2":"","local_mobile":"","mem_id":2,"id":30667660,"loc":"上海","ouid":2953747336,"mmid":"30667660","utype":1,"mem_st":1,"line4":"金融 | 销售/理财, 影响力: 177","line3":"宝付支付跨境支付高级商户经理(上海)","compos":"宝付支付跨境支付高级商户经理","line1":"宝付支付跨境支付高级商户经理","in_app":1,"lv":0,"is_co":"false","tid":"mQcnAhda5k","status":1,"is_hp":"false","city":"浦东新区","cmf_no6":0,"company":"宝付支付","short_compos":"宝付支付跨境支付高级商户经理","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozMDY2NzY2MCwibGV2ZWwiOjAsInQiOiJjdHQifQ.0qtgeNMrIRB3D-OAh7mhrCuaL_Ph8MW69MpqoX7Lxao","judge":1,"is_sh":"false","qp":1.4580299854278564,"name":"蒋锐","career":"宝付支付跨境支付高级商户经理","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/2854/1915_12_G13XZunkA5sV3C-a160","is_exco":"false","cmf":0,"position":"跨境支付高级商户经理","job_line":"","short_career":"宝付支付跨境支付高级商户经理"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4931/4301_12_ib5w0XGwyFq8LB","likes":450,"id":227673991,"crtime":"2017-12-20 10:48:28","pic_infos":"49314299,750,900"},{"uid":39581318,"title":"敢","text":"敢，勇也，是敢于面对，是敢于承担，是敢于尝试，是敢于挑战，是敢于创新。我是一个靠理想而生活的人。没有想象力的生活犹如一潭死水，缺少想象力的工作必定是一场牢狱之灾，匮乏想象力的设计师无异于一台美工机器。敢于想象，生活和工作将充满无限可能与希望。最初接到恒大冰泉新品设计任务时，几家设计公司80余款失败的案例摆在眼前，也害怕过、犹豫过、怀疑过。在机遇面前，不在于会不会，而在于敢不敢。“后悔做了总比后悔没做要好”是我一直笃信的教条。我相信一切都会更好，2017一切安好，2018将会更好。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4930/7847_6_k1Hq01bxd3d89v","turl":"http://i9.taou.com/maimai/p/4930/7847_6_k1Hq01bxd3d89v-t480","y":900,"x":750}],"uinfo":{"province":"广东","major":6,"py":"yang2杨zhao4赵jun1军","dist":0,"figure":45242217,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":148,"line2":"","local_mobile":"","mem_id":2,"id":39581318,"loc":"广东","ouid":3759332256,"mmid":"39581318","utype":1,"cmf_no6":0,"line4":"IT互联网 | 设计, 影响力: 148","line3":"恒大矿泉水集团设计负责人(广东)","compos":"恒大矿泉水集团设计负责人","line1":"恒大矿泉水集团设计负责人","in_app":1,"lv":0,"is_co":"false","tid":"m4d8w8sUUv1","mem_st":0,"status":1,"is_hp":"false","city":"深圳","company":"恒大矿泉水集团","short_compos":"恒大矿泉水集团设计负责人","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozOTU4MTMxOCwibGV2ZWwiOjAsInQiOiJjdHQifQ.G7nEuuZMxYaYnZzGuJeytgABtVJjaVzjyLdH0i4ynLo","judge":1,"is_sh":"false","qp":1.6841100454330444,"name":"杨赵军","career":"恒大矿泉水集团设计负责人","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/4524/2217_6_i1AjArvp5yCGra-a160","is_exco":"false","cmf":0,"position":"设计负责人","job_line":"","short_career":"恒大矿泉水集团设计负责人"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4930/7848_6_qEsDGyb56D9qtz","likes":411,"id":227649376,"crtime":"2017-12-20 10:12:10","pic_infos":"49307847,750,900"},{"uid":32798592,"title":"美","text":"冬日季节，阳光静美，世间依然喧嚣。沏一杯茶，读一本书，品味烟火人生。回想这一年，我没有看过一部剧，没有玩过一次手游。略显无聊却是一种成长。读了好几本书，发了若干篇文，谈不上成就但也算是收获。越来越发现，很多事情往往并没有想象中那么重要，也无须在意。人生不是一时的成与败，也不是短暂的得与失，应当是一种态度，是一种方向。态度摆正就不必犹豫，方向对了就勇往直前。一切的经历，好的与坏的，都应化为成熟藏于心中。烟火人生，红尘一梦。这一年并不完美，却依然很美。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4930/7167_0_H1Wyr5sS1R5P9V","turl":"http://i9.taou.com/maimai/p/4930/7167_0_H1Wyr5sS1R5P9V-t480","y":900,"x":750}],"uinfo":{"province":"上海","major":0,"py":"zou1邹jing4靖yun1贇","dist":0,"figure":26521193,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":1255,"line2":"","local_mobile":"","mem_id":2,"id":32798592,"loc":"上海","ouid":3490686888,"mmid":"32798592","utype":1,"cmf_no6":0,"line4":"IT互联网 | 研发, 影响力: 1255","line3":"蚂蚁金服技术专家(上海)","compos":"蚂蚁金服技术专家","line1":"蚂蚁金服技术专家","in_app":1,"lv":0,"is_co":"false","tid":"m55zpHyNQ8b","mem_st":0,"status":1,"is_hp":"false","city":"浦东新区","company":"蚂蚁金服","short_compos":"蚂蚁金服技术专家","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozMjc5ODU5MiwibGV2ZWwiOjAsInQiOiJjdHQifQ.4o-KfDFto6JEwFBhqokL4QELk9k5nhY6OELfFw0ds1c","judge":1,"is_sh":"false","qp":2,"name":"邹靖贇","career":"蚂蚁金服技术专家","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/2652/1193_0_m1yYYH0cEtc7bI-a160","is_exco":"false","cmf":0,"position":"技术专家","job_line":"","short_career":"蚂蚁金服技术专家"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4930/7170_0_4L8Htz4j0WbNV9","likes":409,"id":227646500,"crtime":"2017-12-20 10:08:05","pic_infos":"49307167,750,900"},{"uid":3083332,"title":"练","text":"2016年，我把自己从舒适的外企独立办公室逼出来，目的是重新激活自己，想在步入中年危机前获取重生的机会和动力。然而，刚开始却陷入了焦灼，转型中遇到了不适应和迷茫。经过2017年的摔打磨练，我从阿里机器人到优酷，从SLAM室内地图到视频理解与植入，从对AI的好奇盲入到对算法落地的现实思考，我看问题的角度转变了，也成长了。现在，我不仅可以将几大块技术融合在一起进行创新突破，还能延伸技术栈，并且可以很好地发挥。愿2017年在这种充满激情的工作状态中结束，也愿2018年我的团队能收获更多牛人的加入。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4930/6818_68_dPbKFeinSIEvrQ","turl":"http://i9.taou.com/maimai/p/4930/6818_68_dPbKFeinSIEvrQ-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":0,"py":"dan1单cheng2成liang4亮","dist":0,"figure":5968332,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":348,"line2":"","local_mobile":"","mem_id":2,"id":3083332,"loc":"北京","ouid":4026629238,"mmid":"3083332","utype":1,"cmf_no6":0,"line4":"IT互联网 | 研发, 影响力: 348","line3":"阿里高级专家(北京)","compos":"阿里高级专家","line1":"阿里高级专家","in_app":1,"lv":0,"is_co":"false","tid":"m1YmlnsFShC","mem_st":0,"status":1,"is_hp":"false","city":"朝阳区","company":"阿里","short_compos":"阿里高级专家","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozMDgzMzMyLCJsZXZlbCI6MCwidCI6ImN0dCJ9.btLQt1UKUKqU809dbtkcEZEcoWqiK4ivtw4vRgPnGvg","judge":1,"is_sh":"false","qp":2.180000066757202,"name":"单成亮","career":"阿里高级专家","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/596/8332_68_3CEeIKMOQRzMVa-a160","is_exco":"false","cmf":0,"position":"高级专家","job_line":"","short_career":"阿里高级专家"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4930/6819_68_i1Xdl7isLPAELu","likes":408,"id":227645377,"crtime":"2017-12-20 10:06:14","pic_infos":"49306818,750,900"},{"uid":5375780,"title":"虚","text":"回首2017，忙忙碌碌，身心俱疲，却真真切切感到一无所获！接不完的电话，来不完的会，收获甚微，实感虚度年华，辜负光阴。\n在路上，还在路上，依然在路上，总在路上。\n再回首，在路上，挺好！","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4934/2920_36_C21pXrYCofxm5E","turl":"http://i9.taou.com/maimai/p/4934/2920_36_C21pXrYCofxm5E-t480","y":900,"x":750}],"uinfo":{"province":"上海","major":18,"py":"chen2陈jing4靖","dist":0,"figure":3726704,"cmf2":"","is_prof":"false","cmf1":"","profession":3,"rank":117,"line2":"","local_mobile":"","mem_id":0,"id":5375780,"loc":"上海","ouid":4026700845,"mmid":"5375780","utype":1,"cmf_no6":0,"line4":"金融 | 高管, 影响力: 117","line3":"上海宁拓投资管理有限公司执行董事兼CEO(上海)","compos":"上海宁拓投资管理有限公司执行董事兼CEO","line1":"上海宁拓投资管理有限公司执行董事兼CEO","in_app":1,"lv":0,"is_co":"false","tid":"mgsz09EUUu","mem_st":0,"status":1,"is_hp":"false","city":"浦东新区","company":"上海宁拓投资管理有限公司","short_compos":"上海宁拓投资管理有限公司执行董事兼CEO","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1Ijo1Mzc1NzgwLCJsZXZlbCI6MCwidCI6ImN0dCJ9.Eg7OcIjn987EdgWfp275Vxhbwc6PnV7qTuCRcn4BB3E","judge":1,"is_sh":"false","qp":2.200000047683716,"name":"陈靖","career":"上海宁拓投资管理有限公司执行董事兼CEO","gender":1,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/372/6704_36_h129eMr7HLJt-a160","is_exco":"false","cmf":0,"position":"执行董事兼CEO","job_line":"","short_career":"上海宁拓投资管理有限公司执行董事兼CEO"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4934/2928_36_r149nMz7OLlttp","likes":397,"id":227835152,"crtime":"2017-12-20 13:36:00","pic_infos":"49342920,750,900"},{"uid":31635914,"title":"累","text":"2017年对于我来讲是历经考验的一年，工作、家庭、个人都发生了很多变故。\r\n说实话，心很累，身体也疲。曾经想过放弃，也埋怨过为什么自己要经历这些。但是到现在自己慢慢的也学会接受，2017年，同样这些因素也是促使我快速成长，学会了收敛脾气，学会了接受现实。2017，马上就要过去了，希望明年能够好一点。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4930/5027_74_G187QOEoz0ybzH","turl":"http://i9.taou.com/maimai/p/4930/5027_74_G187QOEoz0ybzH-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":5,"py":"sun1孙li3礼yuan2媛","dist":0,"figure":44668236,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":787,"line2":"","local_mobile":"","mem_id":2,"id":31635914,"loc":"北京","ouid":2148471258,"mmid":"31635914","utype":1,"mem_st":1,"line4":"IT互联网 | 运营/编辑, 影响力: 787","line3":"脉脉运营(北京)","compos":"脉脉运营","line1":"脉脉运营","in_app":1,"lv":0,"is_co":"false","tid":"m1a2kjHgxkl","status":113,"is_hp":"false","city":"北京","cmf_no6":0,"company":"脉脉","short_compos":"脉脉运营","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozMTYzNTkxNCwibGV2ZWwiOjAsInQiOiJjdHQifQ.YVOWGVKdhJUY3Z2ICEWLlsO0-E610S4Tv2NeKvx9MiE","judge":1,"is_sh":"false","qp":2.0999999046325684,"name":"孙礼媛","career":"脉脉运营","gender":2,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/4466/8236_74_B25wo8aPayuOL8-a160","is_exco":"false","cmf":0,"position":"运营","job_line":"","short_career":"脉脉运营"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4930/5028_74_LFUUwAERs6uHTX","likes":394,"id":227638388,"crtime":"2017-12-20 09:54:46","pic_infos":"49305027,750,900"},{"uid":30349442,"title":"忙","text":"2017，加入了脉脉，就开始了忙忙碌碌的日子，忙到会经常以为又回到了入行的那一年……岁末回望，虽然事情多也很操心，却也也学到了很多。或许，明年依旧忙碌，但大踏步向前的脚步不会停止，更愿岁月不虚度。","image":[{"tx":400,"ty":480,"url":"http://i9.taou.com/maimai/p/4930/1827_2_R1x8CLjJqby2fe","turl":"http://i9.taou.com/maimai/p/4930/1827_2_R1x8CLjJqby2fe-t480","y":900,"x":750}],"uinfo":{"province":"北京","major":9,"py":"liu2刘chen2晨","dist":0,"figure":46280083,"cmf2":"","is_prof":"false","cmf1":"","profession":0,"rank":425,"line2":"","local_mobile":"","mem_id":2,"id":30349442,"loc":"北京","ouid":3222174928,"mmid":"30349442","utype":1,"mem_st":1,"line4":"IT互联网 | 市场商务, 影响力: 425","line3":"脉脉公关总监(北京)","compos":"脉脉公关总监","line1":"脉脉公关总监","in_app":1,"lv":0,"is_co":"false","tid":"m1kgeLGhGDR","status":1,"is_hp":"false","city":"北京","cmf_no6":0,"company":"脉脉","short_compos":"脉脉公关总监","d1type":0,"pub":0,"encode_mmid":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1IjozMDM0OTQ0MiwibGV2ZWwiOjAsInQiOiJjdHQifQ.tycJtfBECw-gUk6Q2aWtdgmqNu52t1ZGW4XKm7RHbHg","judge":1,"is_sh":"false","qp":2.700000047683716,"name":"刘晨","career":"脉脉公关总监","gender":2,"oline2":"","sr":0,"wbname":"","avatar":"http://i9.taou.com/maimai/p/4628/83_2_x1sKPS7Lc0UOzR-a160","is_exco":"false","cmf":0,"position":"公关总监","job_line":"","short_career":"脉脉公关总监"},"mylike":0,"tmp_image":"http://i9.taou.com/maimai/p/4930/1829_2_72XsXlViw7IfHh","likes":374,"id":227625936,"crtime":"2017-12-20 09:33:57","pic_infos":"49301827,750,900"}],"all":72785,"result":"ok"}
json_str = json.dumps(share_data,sort_keys=True,indent=2)

py_str = json.loads(json_str)  # 通过loads方法转化为python对象，然后进行相应的操作。

print(json_str)
print(type(py_str))
print(py_str['feed'])


py_lst = py_str['feed']
i = 0
print(len(py_lst))
for i in range(len(py_lst)):
    print('*'* 100)
    print(i)
    print(py_lst[i]['title'])
    print(py_lst[i]['text'])
    print(py_lst[i]['uinfo']['province'])
    print(py_lst[i]['uinfo']['loc'])
    print(py_lst[i]['uinfo']['compos'])
    print(py_lst[i]['uinfo']['name'])
    print(py_lst[i]['uinfo']['career'])
    print(py_lst[i]['uinfo']['gender'])

    print(py_lst[i]['likes'])
    print(py_lst[i]['crtime'])





