#include <GL/freeglut.h>
#include <iostream>
#include <cmath>
#include <fstream>
#include <gmpxx.h>
#include <string>
using namespace std;


// consts
const float SCALE = 1;
const int ARESX = 1200;
const int ARESY = 700;
const int WRESX = ARESX * SCALE;
const int WRESY = ARESY * SCALE;



// functions
void display();
void fill(unsigned char arr[ARESY][ARESX][3]);
void print(unsigned char arr[ARESY][ARESX][3]);
void bright(unsigned char arr[ARESY][ARESX][3], int n);
void contrast(unsigned char arr[ARESY][ARESX][3], double n);
void blur(unsigned char arr[ARESY][ARESX][3]);
unsigned char inRange(int n);
unsigned char nbrAvg(unsigned char arr[ARESY][ARESX][3], int r, int c, int color);
void sharpen(unsigned char arr[ARESY][ARESX][3]);
unsigned char nbrSharp(unsigned char arr[ARESY][ARESX][3], int r, int c, int color);


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
	
	for(int i = 0; i < 5; i++) {
		blur(arr);
	}
	contrast(arr, 5);

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


void blur(unsigned char arr[ARESY][ARESX][3]) {
	// make temp array
	unsigned char temp[ARESY][ARESX][3];

	// go through original array
	for(int r = 1; r < ARESY-1; r++) {
		for(int c = 1; c < ARESX-1; c++) {
			for(int color = 0; color < 3; color++) {
				int avg = 0;
				avg += arr[r-1][c-1][color];
				avg += arr[r-1][c][color];
				avg += arr[r-1][c+1][color];
				avg += arr[r][c-1][color];
				avg += arr[r][c][color];
				avg += arr[r][c+1][color];
				avg += arr[r+1][c-1][color];
				avg += arr[r+1][c][color];
				avg += arr[r+1][c+1][color];
				temp[r][c][color] = avg / 9.0;
			}
		}
	}
	
	// put temp back into arr
	for(int r = 1; r < ARESY-1; r++) {
		for(int c = 1; c < ARESX-1; c++) {
			for(int color = 0; color < 3; color++) {
				arr[r][c][color] = temp[r][c][color];
			}
		}
	}
}


void bright(unsigned char arr[ARESY][ARESX][3], int b) {
	for(int r = 0; r < ARESY; r++) {
		for(int c = 0; c < ARESX; c++) {
			arr[r][c][0] = inRange(arr[r][c][0] + b);
			arr[r][c][1] = inRange(arr[r][c][1] + b);
			arr[r][c][2] = inRange(arr[r][c][2] + b);
		}
	}
}


void contrast(unsigned char arr[ARESY][ARESX][3], double n) {
	for(int r = 0; r < ARESY; r++) {
		for(int c = 0; c < ARESX; c++) {
			arr[r][c][0] = inRange((arr[r][c][0]-128) * n + 128);
			arr[r][c][1] = inRange((arr[r][c][1]-128) * n + 128);
			arr[r][c][2] = inRange((arr[r][c][2]-128) * n + 128);
		}
	}
}



unsigned char inRange(int n) {
	if(n > 255) {
		return 255;
	} else if (n < 0){
		return 0;
	} else {
		return n;
	}
}


void fill(unsigned char arr[ARESY][ARESX][3]) {
	// original num and den strings
	string n, d;

	// get input
	cout << "Please enter a numerator: ";
	cin >> n;
	cout << "Please enter a denominator: ";
	cin >> d;
	
	// init my mpf classes
	mpf_set_default_prec(ARESX*ARESY*24);
	mpf_class num(n);
	mpf_class den(d);
	mpf_class quot = num / den;

	// convert quotient to string type answer
	mp_exp_t exp;
	string answer = quot.get_str(exp, 2, ARESX*ARESY*24);
	for(int i = 0; i < -exp; i++) {
		answer = "0" + answer;
	}
	
	// save answer in byte sized chunks, convert it to int, and print it
	for(int i = 0; i < ARESX*ARESY*24; i+=8) {
		string chunk = answer.substr(i, 8);
		int byt = strtol(chunk.c_str(), NULL, 2);
		//cout << byt << endl;
		int count = i / 8;
		// to find the correct location in the array in 3D
		arr[(count/3)/ARESX][(count/3)%ARESX][count%3] = byt;
	}

}
