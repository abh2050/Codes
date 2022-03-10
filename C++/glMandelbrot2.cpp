#include <GL/freeglut.h>
#include <iostream>
#include <cmath>
#include <fstream>
#include <complex>
using namespace std;


// consts
const int WRESX = 700;
const int WRESY = 700;
const int ARESX = 700;
const int ARESY = 700;


// functions
void display();
void fill(unsigned char arr[ARESY][ARESX][3]);
void print(unsigned char arr[ARESY][ARESX][3]);
int isBounded(complex <double> C);
void mouse(int button, int state, int x, int y);
void keyboard(unsigned char key, int x, int y);


// vars
double Z = 4;
double ZF = 2;
double X0 = 0;
double Y0 = 0;
int L = 100;


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
	glutMouseFunc(mouse);
	glutKeyboardFunc(keyboard);

	// set up the display function to loop and make an animation
	// glutIdleFunc(glutPostRedisplay);
	
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


void keyboard(unsigned char key, int x, int y) {
	switch(key) {
		case 'l':
			cout << "Please enter an iteration limit: ";
			cin >> L;
			glutPostRedisplay();
			break;
		case 'z':
			cout << "Please enter a zoom factor: ";
			cin >> ZF;
			glutPostRedisplay();
			break;
	}
}


void mouse(int button, int state, int x, int y) {
	if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
		// reset zoom and origin
		X0 = X0 + Z*x/ARESX - Z/2;
		Y0 = Y0 - Z*y/ARESY + Z/2;
		Z /= ZF;
	
		// redraw the screen
		glutPostRedisplay();
	}
	if(button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN) {
		// reset zoom and origin
		X0 = X0 + Z*x/ARESX - Z/2;
		Y0 = Y0 - Z*y/ARESY + Z/2;
		Z *= ZF;
	
		// redraw the screen
		glutPostRedisplay();
	}
}


void fill(unsigned char arr[ARESY][ARESX][3]) {
	for(int r = 0; r < ARESY; r++) {
		for(int c = 0; c < ARESX; c++) {
			complex <double> C(X0 + Z*c/ARESX - Z/2, Y0 + Z*r/ARESY - Z/2);

			int n = isBounded(C);
			arr[r][c][0] = 12*n%256; // red
			arr[r][c][1] = 9*n%256; // green
			arr[r][c][2] = 2*n%256; // blue
		}
	}
}


int isBounded(complex <double> C) {
	// init our sequence
	complex <double> M(0, 0);

	// iterate through the sequence
	int i = 0;
	for(i = 0; i < L; i++) {
		M = M*M + C;

		// check where sequence gets unbounded
		if(M.real()*M.real() + M.imag()*M.imag() > 4) {
			break;
		}
	}
	return i;
}

