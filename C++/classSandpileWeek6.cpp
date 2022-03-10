#include <GL/freeglut.h>
#include <iostream>
#include <cmath>
using namespace std;


// consts
const int WRES = 516;
const int ARES = 129;


// functions
void display();
void color(unsigned char arr[ARES][ARES][3], int sand[ARES][ARES]);
void printArr(unsigned char arr[ARES][ARES][3]);
void fill(int sand[ARES][ARES]);
void topple(int sand[ARES][ARES]);



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
	glutIdleFunc(glutPostRedisplay);
	
	// required to make the thing go 
    glutMainLoop();

	// exit
    return 0;
}



int sand[ARES][ARES];
void display() {
	//  clear all pixels
    glClear (GL_COLOR_BUFFER_BIT);

	// make and fill in array
	static unsigned char arr[ARES][ARES][3] = {0};

	static bool firstTime = true;
	if(firstTime) {
		fill(sand);
		firstTime = false;
	}
	for(int i = 0; i < 100; i++) {
		topple(sand);
	}
	color(arr, sand);

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


void topple(int sand[ARES][ARES]) {
	for(int r = 0; r < ARES; r++) {
		for(int c = 0; c < ARES; c++) {
			// topple if too much sand
			if(sand[r][c] >= 4) {
				// distribute to nbrs or fall off the board
				if(r > 0)
					sand[r-1][c] += sand[r][c] / 4;
				if(r < ARES-1)
					sand[r+1][c] += sand[r][c] / 4;
				if(c > 0)
					sand[r][c-1] += sand[r][c] / 4;
				if(c < ARES-1)
					sand[r][c+1] += sand[r][c] / 4;

				// what's left in sand[r][c]
				sand[r][c] = sand[r][c] % 4;
			}
		}
	}
}



void fill(int sand[ARES][ARES]) {
	// clear the array
	for(int r = 0; r < ARES; r++) {
		for(int c = 0; c < ARES; c++) {
			sand[r][c] = 0;
		}
	}

	// then fill
	sand[ARES/2][ARES/2] = 100000;
}



void color(unsigned char arr[ARES][ARES][3], int sand[ARES][ARES]) {
	// puts a color at every array location
	for(int r = 0; r < ARES; r++) {
		for(int c = 0; c < ARES; c++) {
			switch(sand[r][c]) {
				case 0:  // black
					arr[r][c][0] = 0;
					arr[r][c][1] = 0;
					arr[r][c][2] = 0;
					break;
				case 1:  // red
					arr[r][c][0] = 255;
					arr[r][c][1] = 0;
					arr[r][c][2] = 0;
					break;
				case 2:  // green
					arr[r][c][0] = 0;
					arr[r][c][1] = 255;
					arr[r][c][2] = 0;
					break;
				case 3:  // blue
					arr[r][c][0] = 0;
					arr[r][c][1] = 0;
					arr[r][c][2] = 255;
					break;
				default: // white
					arr[r][c][0] = 255;
					arr[r][c][1] = 255;
					arr[r][c][2] = 255;
			}
		}
	}
}

