#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <io.h>
#include <windows.h>
#include <time.h>

#pragma comment(lib, "winmm.lib")
int main(int argc, char *argv[])
{

  time_t t1, t2, previous_pause_time = 0;

  mciSendString("open music.mp3 type mpegvideo alias file", NULL, 0, NULL);
  int n;
  while (1)
  {
    printf("Press 1 to play the file and press 2 to exit the file.\n");
    scanf("%d", &n);
    if (n == 1)
    {
      //play the audio file
      t1 = time(0);
      mciSendString("play file ", NULL, 0, NULL);

      printf("Audio file playing...\n\n");
    }
    else if (n == 2)
    {
      //close the file and get out of the loop
      mciSendString("close file", NULL, 0, NULL);
      break;
    }
    printf("Press 0 to pause the file and press 2 to exit the file.");
    scanf("%d", &n);
    if (n == 0)
    {
      //pause the audio file
      mciSendString("pause file", NULL, 0, NULL);
      t2 = time(0);
      printf("Audio file paused after %d seconds.\n\n", t2 - t1 + previous_pause_time);
      previous_pause_time += t2 - t1;
    }
    else if (n == 2)
    {
      //close the audio file
      mciSendString("close file", NULL, 0, NULL);
      break;
    }
  }
}