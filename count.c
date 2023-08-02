
 

int exam (int map[], int y, int x, int WIDTH, int HEIGHT)
{
 if(x < 0 || y < 0 || x >= WIDTH || y >= HEIGHT)
 {
  return 0;
 }
 return map[y*WIDTH+x];
}

int count (int map[], int y, int x, int WIDTH, int HEIGHT)
{
 int sum = 0;
 for (int i = y - 1; i < y + 2; i++)
 {
  for (int j = x - 1; j < x + 2; j++)
  {
   if(i >= 0 && j >= 0 && i < HEIGHT && j < WIDTH)
   {
    sum += exam(map, i, j, WIDTH, HEIGHT);
   }
  }
 }
 return sum - map[y*WIDTH+x];
}






