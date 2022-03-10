#include <GL/freeglut.h>
#include <iostream>
#include <cmath>
using namespace std;


// consts
const int WRES = 802;
const int ARES = 401;


// functions
void display();
void fill(unsigned char arr[ARES][ARES][3], int spiral[ARES][ARES]);
void init(int spiral[ARES][ARES]);
int isPrime(int n);


int main(int argc, char** argv) {
    // set up displays and mode (we won't change this!)
	glutInit(&argc, argv);
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
    
	// set window size
	glutInitWindowSize (WRES, WRES); 
    
	// set window position on screen
	glutInitWindowPosition (0, 0);

	// set window title
    glutCreateWindow ("test");
    
    // set the display function to the one we made below
	glutDisplayFunc(display);
	
	// required to make the thing go 
    glutMainLoop();

	// exit
    return 0;
}


void display() {
	//  clear all pixels
    glClear (GL_COLOR_BUFFER_BIT);

	// make and fill in array
	static unsigned char arr[ARES][ARES][3] = {0};
	static int spiral[ARES][ARES] = { 0 };
	init(spiral);
	fill(arr, spiral);

	// resize the array to the size of the window RES
	glPixelZoom((float)WRES/ARES, (float)WRES/ARES);
	
	// unpack wrong??
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
	glPixelStorei(GL_UNPACK_SKIP_PIXELS, 0);
	glPixelStorei(GL_UNPACK_SKIP_ROWS, 0);

	// draw the array to the screen
	glDrawPixels(ARES, ARES, GL_RGB, GL_UNSIGNED_BYTE, arr);

	// start processing buffered OpenGL routines 
    glFlush ();
}


void fill(unsigned char arr[ARES][ARES][3], int spiral[ARES][ARES]) {
	// puts a color at every array location
	for(int r = 0; r < ARES; r++) {
		for (int c = 0; c < ARES; c++) {
			arr[r][c][0] = 5 * isPrime(spiral[r][c]); // red
			arr[r][c][1] = 11 * isPrime(spiral[r][c]); // green
			arr[r][c][2] = 13 * isPrime(spiral[r][c]); // blue
		}
	}
}


int isPrime(int n) {
	int divCount = 0;
	for (int div = 2; div*div <= n; div++) {
		if (n % div == 0) {
			divCount += 2;
		}
	}
	return divCount;
}


void init(int spiral[ARES][ARES]) {
	// vars
	int num = 1;
	int dist = 1;
	int row = ARES / 2;
	int col = ARES / 2;

	spiral[row][col] = num; // do the middle

	for (int j = 0; j < (ARES - 1) / 2; j++) {
		for (int i = 0; i < dist; i++) {
			spiral[row][++col] = ++num;    // right
		}
		for (int i = 0; i < dist; i++) {
			spiral[--row][col] = ++num;    // down
		}

		dist++; // increment distance

		for (int i = 0; i < dist; i++) {
			spiral[row][--col] = ++num;    // left
		}
		for (int i = 0; i < dist; i++) {
			spiral[++row][col] = ++num;    // up
		}

		dist++; // increment distance again
	}

	// fill in the top row
	for (int i = 0; i < dist - 1; i++) {
		spiral[row][++col] = ++num;
	}
}