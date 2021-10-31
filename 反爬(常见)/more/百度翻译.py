# Python中执行js的方法 execjs js2py
import json

import js2py
import requests
import re
# 分析百度js逆向  发现sign执行了某个方法
# 我们可以使用Python操作js来代替我们使用这个方法
# 最后获取到这个方法返回出来的值
from jsonpath import jsonpath

jsdata = r'''
 function n(r, o) {
        for (var t = 0; t < o.length - 2; t += 3) {
            var a = o.charAt(t + 2);
            a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
            a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
            r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
        }
        return r
    }
 function e(r) {  
        i = "320305.131321201"
        var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
        if (null === o) {
            var t = r.length;
            t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
        } else {
            for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                C !== h - 1 && f.push(o[C]);
            var g = f.length;
            g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
        }
        var u = void 0
          , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
        u = null !== i ? i : (i = window[l] || "") || "";
        for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
            var A = r.charCodeAt(v);
            128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
            S[c++] = A >> 18 | 240,
            S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
            S[c++] = A >> 6 & 63 | 128),
            S[c++] = 63 & A | 128)
        }
        for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
            p += S[b],
            p = n(p, F);
        return p = n(p, D),
        p ^= s,
        0 > p && (p = (2147483647 & p) + 2147483648),
        p %= 1e6,
        p.toString() + "." + (p ^ m)
    }
'''
url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
headers = {
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Cookie': 'BIDUPSID=180235799AE4B9E72146EDD3FE9D049D; PSTM=1620633041; __yjs_duid=1_412934892873fca7c6d32b45bffdcc4e1620638894720; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=28EEAA0ABCF1FAD66452B268596E50C5:FG=1; H_WISE_SIDS=107317_110085_127969_128698_131423_154213_165135_165518_165935_166147_169066_170816_170872_171509_171565_171706_172473_172643_173017_173612_173773_174037_174179_174449_174618_174665_174682_174695_175231_175276_175283_175343_175364_175467_175545_175667_175755_175898_175929_175948_176129_176131_176157_176187_176194_176263_176345_176399_176554_176563_176765; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1622292450; BDUSS=hjc1RmM0tZQ35adjE2OG5RWDN-Mlp4U0Foc1VnT2YxdG9GOFlZVXpaeW9DT3hnRVFBQUFBJCQAAAAAAAAAAAEAAADEjCc2YnVn7OFxeW0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKh7xGCoe8RgRl; BDUSS_BFESS=hjc1RmM0tZQ35adjE2OG5RWDN-Mlp4U0Foc1VnT2YxdG9GOFlZVXpaeW9DT3hnRVFBQUFBJCQAAAAAAAAAAAEAAADEjCc2YnVn7OFxeW0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKh7xGCoe8RgRl; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; MCITY=-158%3A; BAIDUID_BFESS=28EEAA0ABCF1FAD66452B268596E50C5:FG=1; BDRCVFR[EiXQVvOKA3D]=mk3SLVN4HKm; delPer=0; PSINO=6; H_PS_PSSID=31660_26350; BA_HECTOR=8020a4ak002h0420471gd13i20q; BCLID=6956194346376008689; BDSFRCVID=1e_OJexroG38EYbeF0JKIGLvuuweG7bTDYLtOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JRAjoK-XJDvDqTrP-trf5DCShUFsqPRRB2Q-XPoO3KO4VMI6bfjHMn0IQxJK54QiWbRM2MbgylRM8P3y0bb2DUA1y4vpKh5ma2TxoUJ25DnJ8Jjcqq7ohb8ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hC8xj685DTbM-l-X5to05TIX3b7Efh7bMh7_bJ7KhUbyeMc9BtQlKGnpal3xyP-bspCm5ToxQhFT5-nfXpOe-n7rKhc1QJ34eMoHQT3m5-Ipjt7PtPjr-eC8Wb3cWhRV8UbSKMRPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JDMr0eGKeJTKJtbAfVbobHJoHjJbGq4bohjP_Q4v9BtQO-DOxoKnEBhcqsRjy5Mrn0hk3jPJutn-tQgnk2PbvbMnmqPtRXMJkXhKs3xON0x-jLTnBaD5dQCbD8-oqetnJyUPThtnnBnOi3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CFhfbo5KRopMtOhq4tehH4DKlR9WDTOQJ7TtKnpoJoNQ63kyUF1Xhjt-Rb-3bva-pbwBPbcfUnMKn05XM-pXbjZKxtq3mkjbPbbt66fstKzQf7Mb-4syPRr2xRnWTRiKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCcjqR8Zj5Kbe53P; BCLID_BFESS=6956194346376008689; BDSFRCVID_BFESS=1e_OJexroG38EYbeF0JKIGLvuuweG7bTDYLtOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=JRAjoK-XJDvDqTrP-trf5DCShUFsqPRRB2Q-XPoO3KO4VMI6bfjHMn0IQxJK54QiWbRM2MbgylRM8P3y0bb2DUA1y4vpKh5ma2TxoUJ25DnJ8Jjcqq7ohb8ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hC8xj685DTbM-l-X5to05TIX3b7Efh7bMh7_bJ7KhUbyeMc9BtQlKGnpal3xyP-bspCm5ToxQhFT5-nfXpOe-n7rKhc1QJ34eMoHQT3m5-Ipjt7PtPjr-eC8Wb3cWhRV8UbSKMRPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JDMr0eGKeJTKJtbAfVbobHJoHjJbGq4bohjP_Q4v9BtQO-DOxoKnEBhcqsRjy5Mrn0hk3jPJutn-tQgnk2PbvbMnmqPtRXMJkXhKs3xON0x-jLTnBaD5dQCbD8-oqetnJyUPThtnnBnOi3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CFhfbo5KRopMtOhq4tehH4DKlR9WDTOQJ7TtKnpoJoNQ63kyUF1Xhjt-Rb-3bva-pbwBPbcfUnMKn05XM-pXbjZKxtq3mkjbPbbt66fstKzQf7Mb-4syPRr2xRnWTRiKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCcjqR8Zj5Kbe53P; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1623934180,1624003534,1624262819,1624280645; Hm_lvt_246a5e7d3670cfba258184e42d902b31=1624281604; Hm_lpvt_246a5e7d3670cfba258184e42d902b31=1624281604; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1624282443; ab_sr=1.0.1_NTA3ZWI3NTg2OWYzMDJhZmQxMGEwMmQzNDc0YzNkNzQwZDY0ZDljZjBlNzgzZjdlYTY4OGY5NTMyMWNhOTE5YjMzYzMxNWRmMzg4ZTViODY5OTA0NDVjMGQyYmUzYTJjOGRlY2YxYTNjZjg3ODZiYTE4YWQ1Yzg2NzBhNTkxOWE0MjliNTFhNzMwNDAzNDY5MWI1M2M1YTBhZDkxN2ZiYw==; __yjs_st=2_NjRkOTY2ZmJlZDcwYmVjZGI3ZGIzZDkxYzdjODFiMzg0ZmQ1MjBmOWUzNWQ1ZGY4OGI5ODQ1ZTM3MjY2MDg0ZWZhNTdhOWY1OTlhZGMxOGQ5NDM4ZjM0MjM5YWYzM2Y4N2IwMTRkNDk4OGVkNzhmZGJiMThiNzI3OWQ2YzE1MmVlZmEwYTBhNzViYTVkMjE3MjJhYWRlZDRhYWMyMGFjNzUzNzQzZmJkOGU0ZjZjOTY3ZTM4MTI1NmE1YWFiN2NmMDMyZjA3NTQ4ZDAxN2RhOWMwZjEyMGVhZTkzY2E3ZTVjZDk3YTBmNjkwODgyZjE2OWVmMTRkYjEyZjI4Yjg0Ml83XzIyODRhZGYx'
}
# 生成js解释器
js = js2py.EvalJs()
# 使用js代码
js.execute(jsdata)
def get_fanyi():
    # 他有参数  使用js里面的e函数 并且带一个参数
    query = input('请输入你要查询的值：')
    sign = js.e(query)

    data = {
        'from': 'en',
        'to': 'zh',
        'query': query,
        'transtype': 'translang',
        'simple_means_flag': '3',
        'sign': sign,
        'token': 'c212a71c5ff7685593856b5f8a66ec63',
        'domain': 'common'
    }

    res = requests.post(url,data=data,headers=headers)
    # result = re.findall(r'"dst":"(.*?)"',res.content.decode())[0]
    print(jsonpath(json.loads(res.content.decode()),'$..dst')[0])

while True:
    get_fanyi()