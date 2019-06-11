#include <stdio.h>
#include <stdlib.h>



int parent[800*800];
int xr[4]={1,0,-1,0};
int yr[4]={0,1,0,-1};
int n,m;
int graph[800][800];
int levels[2000];
int vysledok;
int q;


int Find(int x)
{
    if(x==parent[x])
    {

        return x;
    }
    else {
        parent[x]=Find(parent[x]);
        return parent[x];
    }
}
struct Node
{
	int x,y;
	int val;
}nodes[800*800];

int compare(const void *s1, const void *s2)
{
      struct Node *e1 = (struct Node *)s1;
      struct Node *e2 = (struct Node *)s2;
        return e1->val > e2->val;
}

void solve(int q){
    int k = n*m-1;
    int i;
for (i = q-1;i>=0;i--)
		{

		 //   printf("I am here");
			if (nodes[k].val > levels[i])
			{
				while (k>=0 && nodes[k].val > levels[i] )
				{
					int pos = nodes[k].x*m+nodes[k].y;
                    if (!~parent[pos])
						parent[pos]=pos,vysledok++;
                    int di;
					for ( di=0;di<4;di++)
					{
					    int dx = nodes[k].x + xr[di];
					    int dy = nodes[k].y+ yr[di];

						if (dx>=0 && dx< n && dy >=0 && dy <m && graph[dx][dy]> levels[i])
						{
							int ppos = dx*m+dy;
						    if (~parent[ppos])
						    {
							   int u = Find(ppos);
							   int v = Find(pos);
							   if (u!=v)
							    	parent[u]=v, vysledok--;
						    }
						}
					}
					k--;
				}
				if (k<0)
				{
					for (;i>=0;i--)
					{
						levels[i]=vysledok;
					}
					break;
				}
		  	}
			levels[i]=vysledok;
		 }
}

void print(int q)
{
    int i;
        for (i = 0;i<q;i++)
        {
            printf("%d ",levels[i]);
        }
printf("\n");
}

void createHeap()
{
    scanf("%d %d",&n,&m);
    int i, j;
    	for (i = 0;i<n;i++){

			for (j = 0;j<m;j++)
			{
				scanf("%d",&graph[i][j]);
				int pos = i*m+j;
				nodes[pos].x=i;
				nodes[pos].y=j;
				nodes[pos].val=graph[i][j];
			}
    }
}

void makeLevels()
{
	
    scanf("%d",&q);
    int i;
   	for ( i = 0;i<q;i++)
        {
            scanf("%d",&levels[i]);
        }
		    int x;
    for(x=0; x<10;x++){}
}
int main()
{
    int t;
	scanf("%d",&t);
	int z;
	for(z=0;z < t; z++ )
    {
        createHeap();
        vysledok = 0;
	makeLevels();
    int x;
    for(x=0; x<10;x++){}
	memset(parent,-1,sizeof(parent));
	qsort(nodes, n*m, sizeof(struct Node), compare);
    solve(q);
    print(q);
		//printf("fffff");
		//printf("%d", sizeof(nodes[0]));
	//	printf("size is %d", nodes + n*m);
         //   printf("node size is %d\n", sizeof(struct Node));
//        size_t structs_len = sizeof(nodes) / sizeof(struct st_ex);
      //  printf("fff");

     //   printf("%d %d %d %d\n", nodes[0].val,nodes[1].val, nodes[2].val, nodes[3].val);
		//
	}
}