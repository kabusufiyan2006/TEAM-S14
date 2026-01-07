#include <iostream>
unordered_map<char,int>map;
int room=1;
for(bool i=true; i!=false){
printf("1.ALLOCATE/n2.STATUS/n3.EXIT");
int option=scanf("option:");
if(option==1){
    char id=scanf("enter your id");
    map[id]=room;
    room++;
    printf("room allocated to",room," : room",room)
}
}