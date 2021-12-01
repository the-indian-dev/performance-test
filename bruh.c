#include <stdio.h>

int add(int a, int b){
	return a + b;
}

int main(){
	int b;
	b = add(1,2);
	printf("%d", b);
	return 0;
}
