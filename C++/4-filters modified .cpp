#include <GL/freeglut.h>
#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;


// consts
const int ARESX = 630;
const int ARESY = 354; 
const int WRESX = 630;
const int WRESY = 354;


// functions
void display();
void fill(unsigned char arr[ARESY][ARESX][3]);
void brightness(unsigned char arr[ARESY][ARESX][3], int b);
void contrast(unsigned char arr[ARESY][ARESX][3], double b);
void blurSharpen(unsigned char arr[ARESY][ARESX][3], int b);
unsigned char avgNbr(unsigned char arr[ARESY][ARESX][3], int r, int c, int color);
unsigned char unNbr(unsigned char arr[ARESY][ARESX][3], int r, int c, int color);


int main(int argc, char** argv) {
    // set up displays and mode (we won't change this!)
	glutInit(&argc, argv);
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
    
	// set window size
	glutInitWindowSize (WRESX, WRESY); 
    
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
	static unsigned char arr[ARESY][ARESX][3] = {0};
	fill(arr);
	blurSharpen(arr, 0);
	brightness(arr, 40);
	contrast(arr, 2);

	// resize the array to the size of the window RES
	glPixelZoom((float)WRESX/ARESX, (float)WRESY/ARESY);
	
	// unpack wrong??
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
	glPixelStorei(GL_UNPACK_SKIP_PIXELS, 0);
	glPixelStorei(GL_UNPACK_SKIP_ROWS, 0);

	// draw the array to the screen
	glDrawPixels(ARESX, ARESY, GL_RGB, GL_UNSIGNED_BYTE, arr);

	// start processing buffered OpenGL routines 
    glFlush ();
}


unsigned char avgNbr(unsigned char arr[ARESY][ARESX][3], int r, int c, int color) {
	int result = 0;
	result += arr[r - 1][c - 1][color];
	result += arr[r - 1][c][color];
	result += arr[r - 1][c + 1][color];
	result += arr[r][c - 1][color];
	result += arr[r][c][color];
	result += arr[r][c + 1][color];
	result += arr[r + 1][c - 1][color];
	result += arr[r + 1][c][color];
	result += arr[r + 1][c + 1][color];
	return result / 9;
}


unsigned char unNbr(unsigned char arr[ARESY][ARESX][3], int r, int c, int color) {
	int result = 0;
	result -= arr[r - 1][c - 1][color];
	result -= arr[r - 1][c][color];
	result -= arr[r - 1][c + 1][color];
	result -= arr[r][c - 1][color];
	result -= arr[r][c][color];
	result -= arr[r][c + 1][color];
	result -= arr[r + 1][c - 1][color];
	result -= arr[r + 1][c][color];
	result -= arr[r + 1][c + 1][color];
	return result;
}


void blurSharpen(unsigned char arr[ARESY][ARESX][3], int b) {
	// to blur multiple times
	for (int i = 0; i < b; i++) {
		unsigned char static temp[ARESY][ARESX][3] = { 0 };
		for (int r = 1; r < ARESY-1; r++) {
			for (int c = 1; c < ARESX-1; c++) {
				temp[r][c][2] = unNbr(arr, r, c, 2); // red
				temp[r][c][1] = unNbr(arr, r, c, 1); // green
				temp[r][c][0] = unNbr(arr, r, c, 0); // blue
			}
		}

		for (int r = 1; r < ARESY-1; r++) {
			for (int c = 1; c < ARESX-1; c++) {
				arr[r][c][2] = temp[r][c][2]; // red
				arr[r][c][1] = temp[r][c][1]; // green
				arr[r][c][0] = temp[r][c][0]; // blue
			}
		}
	}
}


unsigned char inRange(int n) {
	if (n > 255) {
		return 255;
	} else if (n < 0) {
		return 0;
	} else {
		return n;
	}
}


void brightness(unsigned char arr[ARESY][ARESX][3], int b) {
	for (int r = 0; r < ARESY; r++) {
		for (int c = 0; c < ARESX; c++) {
			arr[r][c][2] = inRange(arr[r][c][2] + b); // red
			arr[r][c][1] = inRange(arr[r][c][1] + b); // green
			arr[r][c][0] = inRange(arr[r][c][0] + b); // blue
		}
	}
}


void contrast(unsigned char arr[ARESY][ARESX][3], double b) {
	for (int r = 0; r < ARESY; r++) {
		for (int c = 0; c < ARESX; c++) {
			arr[r][c][2] = inRange((arr[r][c][2] - 128) * b + 128);
			arr[r][c][1] = inRange((arr[r][c][1] - 128) * b + 128);
			arr[r][c][0] = inRange((arr[r][c][0] - 128) * b + 128);
		}
	}
}


void fill(unsigned char arr[ARESY][ARESX][3]) {
	// file reading stream
	ifstream file;
	file.open("C:/Users/shahabhi/OneDrive - Intel Corporation/Desktop/C++/HW4/tiger.bmp", ios::binary);

	// make sure file opened
	if (file.is_open()) {
		cout << "it opened!";
	}

	file.ignore(54); // skip the heading

	// puts a color at every array location
	for(int r = 0; r < ARESY; r++) {
		for(int c = 0; c < ARESX; c++) {
			arr[r][c][2] = file.get(); // red
			arr[r][c][1] = file.get(); // green
			arr[r][c][0] = file.get(); // blue
		}
		
		// skip the EOL 
		if ((3 * ARESX) % 4 != 0) {
			file.ignore(4 - (3 * ARESX) % 4);
		}
	}
}


