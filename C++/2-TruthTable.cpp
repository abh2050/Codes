#include <GL/freeglut.h>
#include <iostream>
#include <cmath>
using namespace std;


// consts
const int WRES = 512;
const int VARS = 3;
const int ARES = 24;


// functions
void display();
void fill(unsigned char arr[ARES][ARES][3]);
bool isTrue(int r, int c);
bool cond(bool P, bool Q);



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
	fill(arr);

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


void fill(unsigned char arr[ARES][ARES][3]) {
	// puts a color at every array location
	for(int r = 0; r < ARES; r++) {
		for(int c = 0; c < ARES; c++) {
			bool val = isTrue(r, c);
			arr[r][c][0] = 55 * val; // red
			arr[r][c][1] = 155 * val; // green
			arr[r][c][2] = 105 * val; // blue
		}
	}
}


bool isTrue(int r, int c) {
	// temp var to hold the row
	int temp = r;

	// set up an array to hold the variables
	bool arr[VARS] = { 0 };

	// fill the array with the correct t/f values for that row
	for (int count = VARS-1; count >= 0; count--) {
		arr[count] = temp % 2;
		temp = temp / 2;
	}

	// return if a simple variable
	switch(c/6) {
	case 0:
		return arr[c];
	case 1:
		return !arr[c % 6];
	case 2:
		return !arr[5 - c % 6];
	case 3:
		return arr[5 - c % 6];
	case 4:
		return arr[c % 6];
	case 5:
		return !arr[c % 4];
	case 6:
		return !arr[5 - c % 6];
	case 7:
		return arr[5 - c % 6];
	case 8:
		return arr[c % 6];
	case 9:
		return !arr[c % 6];
	case 10:
		return !arr[5 - c % 6];
	}

	/*
	switch (c/16) {
	case 0:
		return arr[rand()%6]; // and
	case 1:
		return cond(arr[rand() % 6], arr[rand() % 6]);
	case 2:
		return cond(cond(arr[rand() % 6], arr[rand() % 6]), arr[rand() % 6]); // bicon
	case 3:
		return cond(cond(cond(arr[rand() % 6], arr[rand() % 6]), arr[rand() % 6]), arr[rand() % 6]); // or
	default:
		return 0;
	}*/

	//do the formulas
	switch (c) {
	case 0:
		return arr[1];
	case 1:
		return !arr[2];
	case 2:
		return !arr[3];
	case 3:
		return arr[0] || arr[1]; // P or Q
	case 4:
		return arr[0] && arr[1]; // P and Q
	case 5:
		return cond(arr[0], arr[1]); // P -> Q
	case 6:
		return arr[1] == arr[2]; // Q <-> R
	case 7:
		return arr[1] != arr[2]; // P xor R
	}
}


bool cond(bool P, bool Q) {
	return !P || Q;
}

