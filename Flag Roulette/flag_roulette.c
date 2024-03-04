
void win(void)
{
  puts("You won");
  puts("Like, actually won");
  puts("You are not supposed to win");
  puts("You probably cheated, this function is not supposed to get called");
  /* WARNING: Subroutine does not return */
  exit(0);
}

void lose(void)
{
  puts("You lose, and we win");
  /* WARNING: Subroutine does not return */
  exit(0);
}


void main(void)
{
  int iVar1;
  long in_FS_OFFSET;
  void *local_2c;
  char local_2b;
  char local_2a;
  char local_29;
  uint local_28;
  uint local_24;
  uint local_20;
  uint local_1c;
  void *local_18;

  local_10 = *(undefined8 *)(in_FS_OFFSET + 0x28);
  banner();
  local_2b = '\0';
  do {
    while( true ) {
      do {
        while( true ) {
          menu();
          local_2a = 0;
          local_29 = '\0';
          iVar1 = getchar();
          local_2a = (char)iVar1;
          while (local_2a == '\n') {
            iVar1 = getchar();
            local_2a = (char)iVar1;
          }
          while (local_29 != '\n') {
            iVar1 = getchar();
            local_29 = (char)iVar1;
          }
          if (local_2a != '3') break;
          if (local_2b == '\0') {
            puts("You have not placed a bet !");
          }
          else {
            printf("Your bet : %s\n",local_18);
            for (local_1c = 0; local_1c < local_24; local_1c = local_1c + 3) {
              if (*(char *)((long)local_18 + (ulong)local_1c) != 'G') {
                lose();
              }
              if (*(char *)((long)local_18 + (ulong)(local_1c + 1)) != 'C') {
                lose();
              }
              if (*(char *)((long)local_18 + (ulong)(local_1c + 2)) != 'C') {
                lose();
              }
            }
            win();
          }
        }
      } while ('3' < local_2a);
      if (local_2a == '1') break;
      if (local_2a == '2') {
        if (local_2b == '\0') {
          puts("You have no bet placed");
        }
        else {
          free(local_18);
          local_18 = (void *)0x0;
          puts("Bet successfully deleted");
          local_2b = '\0';
        }
      }
    }
    if (local_2b == '\x01') {
      puts("You already have a bet placed");
    }
    else {
      puts("How many bytes would you like to bet on ?");
      printf("> ");
      __isoc99_scanf(&DAT_0010226a,&local_24);
      if ((int)local_24 < 0x80) {
        puts("Not enough bytes");
        puts("The bet is not risky enough");
      }
      else if ((int)local_24 < 0x21001) {
        local_18 = malloc((long)(int)local_24);
        for (local_20 = 0; local_20 < local_24; local_20 = local_20 + 1) {
          iVar1 = rand();
          *(char *)((long)local_18 + (ulong)local_20) = (char)iVar1;
          while ((*(char *)((long)local_18 + (ulong)local_20) < ' ' ||
                 (*(char *)((long)local_18 + (ulong)local_20) == '\x7f'))) {
            iVar1 = rand();
            *(char *)((long)local_18 + (ulong)local_20) = (char)iVar1;
          }
        }
        puts("Random pattern generated successfully");
        puts(
            "\nAs a sign of good will, we will let you modify set exactly one byte in this sea of ra ndomness"
            );
        puts("Please choose the index of the byte to modify");
        printf("> ");
        __isoc99_scanf(&DAT_0010226a,&local_28);
        puts("Please set the new value of this byte");
        printf("> ");
        __isoc99_scanf(&DAT_0010226a,&local_2c);
        *(undefined *)((ulong)local_28 + (long)local_18) = local_2c;
        puts("Modification successful");
        local_2b = '\x01';
      }
      else {
        puts("Come on, you cannot be THAT lucky ;)");
      }
    }
  } while( true );
}
