#include <GL/freeglut.h>
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;


// consts
const int WRES = 512;
const int ARES = 122;


// functions
void display();
void color(unsigned char arr[ARES][ARES][3], int spiral[ARES][ARES]);
void fill(int spiral[ARES][ARES]);
int isPrime(int n);


int main(int argc, char** argv) {
	// set up displays and mode (we won't change this!)
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	// set window size
	glutInitWindowSize(WRES, WRES);

	// set window position on screen
	glutInitWindowPosition(0, 0);

	// set window title
	glutCreateWindow("test");

	// set the display function to the one we made below
	glutDisplayFunc(display);

	// required to make the thing go
	glutMainLoop();

	// exit
	return 0;
}


void display() {
	//  clear all pixels
	glClear(GL_COLOR_BUFFER_BIT);

	// make and fill in array
	static unsigned char arr[ARES][ARES][3] = { 0 };
	static int spiral[ARES][ARES] = { 0 };
	fill(spiral);
	color(arr, spiral);

	// resize the array to the size of the window RES
	glPixelZoom((float)WRES / ARES, (float)WRES / ARES);

	// unpack wrong??
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
	glPixelStorei(GL_UNPACK_SKIP_PIXELS, 0);
	glPixelStorei(GL_UNPACK_SKIP_ROWS, 0);

	// draw the array to the screen
	glDrawPixels(ARES, ARES, GL_RGB, GL_UNSIGNED_BYTE, arr);

	// start processing buffered OpenGL routines
	glFlush();
}


void color(unsigned char arr[ARES][ARES][3], int spiral[ARES][ARES]) {
	// puts a color at every array location
	for (int r = 0; r < ARES; r++) {
		for (int c = 0; c < ARES; c++) {
			int divs = isPrime(spiral[r][c]);
			if (divs < 4) {
				arr[r][c][0] = 128 * divs; // red
			}
			else if (divs < 8) {
				arr[r][c][1] = 64 * divs; // green
			}
			else {
				arr[r][c][2] = 32 * divs; // blue
			}
			//cout << setw(3) << spiral[ARES-r-1][c];
		}
		//cout << endl;
	}
}


void fill(int spiral[ARES][ARES]) {
	// declare vars
	int x = ARES / 2;
	int y = ARES / 2;
	int num = 1;

	// place the central 1
	spiral[y][x] = num++;

	// main spiral loop
	for (int n = 1; n < ARES; n += 2) {
		// four parts:
		// right n steps
		for (int i = 0; i < n; i++) {
			spiral[y][++x] = num++;
		}
		// up n steps
		for (int i = 0; i < n; i++) {
			spiral[++y][x] = num++;
		}
		// left n+1 steps
		for (int i = 0; i < n + 1; i++) {
			spiral[y][--x] = num++;
		}
		// down n+1 steps
		for (int i = 0; i < n + 1; i++) {
			spiral[--y][x] = num++;
		}
	}

	// go last ARES-1 to the right on the top row
	for (int c = 1; c < ARES; c++) {
		spiral[0][c] = num++;
	}
}


int isPrime(int n) {
	for (int i = 2; i*i <= n; i++) {
		if (n % i == 0) {
			return i;
		}
	}
	return n;
}
