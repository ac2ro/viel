from core.prompt import RavePrompt as prompt , Colors
from threading import Thread
import requests , time
from uuid import uuid4

DIM = Colors.GRAY
PURPLE = Colors.PURPLE
END = Colors.END

GX_USERAGENT = {
    "Content-Type": "application/json",
    "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
}

GX_URL = 'https://api.discord.gx.games/v1/direct-fulfillment'

PROMO_URL = 'https://discord.com/billing/partner-promotions/1180231712274387115/{}'

def get_partner_user_id():

    return {'partnerUserId' : str(uuid4())}

class Viel:

    generated = 0


def generate():
    while True:
        try:
            req = requests.post(GX_URL , headers = GX_USERAGENT , json = get_partner_user_id())

            if not req.status_code == 200: return

            token = req.json().get('token')

            link = PROMO_URL.format(token)

            Viel.generated += 1

            prompt.set_title('Viel Gen | {} Generated Codes.'.format(Viel.generated))

            prompt.print_plus(f'Generated {PURPLE}{Viel.generated}{END} links {DIM}[{END}{PURPLE}{token[-10:]}{END}{DIM}]{END}')

            open('./data/nitro.txt' , 'a').write('{}\n'.format(link))
        except:

            pass
    




def main():

    prompt.clear()

    prompt.print_seperator()
    prompt.sexy_logo()
    prompt.print_prefix('Meta' , 'made by ac2ro :3')
    prompt.print_seperator()

    threads = prompt.ask('Threads')

    try:

        thread_count = int (threads)
    
    except:

        prompt.print_mult('Invalid thread count , Defaulting to 1 Thread.')

        thread_count = 1

    for _ in range(thread_count):
        thr = Thread (target = generate , daemon = True , name = 'Generator Thread')
        thr.start()
        
    prompt.print_prefix('Tip' , 'Press CTRL + C to stop the generator.')


    try:

        while True:
            pass
    
    except (KeyboardInterrupt):
        prompt.vert('Viel' , Genrated = f'{Viel.generated} links')
        exit(0)


    


main()
