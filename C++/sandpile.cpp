#include <GL/freeglut.h>
#include <iostream>
#include <cmath>
using namespace std;


// consts
const int WRES = 808;
const int ARES = 512;


// functions
void display();
void fill4(unsigned char arr[ARES][ARES][3]);
void fill8(unsigned char arr[ARES][ARES][3]);
void fill3d(unsigned char arr[ARES][ARES][3]);
void init();
void topple4();
void topple8();
void topple3d();


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
	glutIdleFunc(display);

	// required to make the thing go 
    glutMainLoop();

	// exit
    return 0;
}


void display() {
	//  clear all pixels
    glClear (GL_COLOR_BUFFER_BIT);

	// check for and do init
	static bool notInit = true;
	if (notInit) {
		init();
		notInit = false;
	}

	// make and fill in array
	static unsigned char arr[ARES][ARES][3] = {0};
	for (int i = 0; i < 100; i++) {
		topple4();
	}
	fill4(arr);

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

int sand[ARES][ARES] = { 0 };
int sand3d[ARES][ARES][ARES] = { 0 };

void init() {
	sand[ARES / 2][ARES / 2] = 100000;
	//sand[ARES / 4][ARES / 4] = 100000;
	//sand[3 * ARES / 4][3 * ARES / 4] = 100000;
	//sand[ARES / 4][3 * ARES / 4] = 100000;
	//sand[3 * ARES / 4][ARES / 4] = 100000;
}



void topple3d() {
	for (int r = 0; r < ARES; r++) {
		for (int c = 0; c < ARES; c++) {
			for (int d = 0; d < ARES; d++) {
				if (sand3d[r][c][d] >= 6) {
					int spillage = sand3d[r][c][d] / 6;

					if (r < ARES - 1) sand3d[r + 1][c][d] += spillage;
					if (r > 0)        sand3d[r - 1][c][d] += spillage;
					if (c < ARES - 1) sand3d[r][c + 1][d] += spillage;
					if (c > 0)        sand3d[r][c - 1][d] += spillage;
					if (d < ARES - 1) sand3d[r][c][d + 1] += spillage;
					if (d > 0)        sand3d[r][c][d - 1] += spillage;

					sand3d[r][c][d] %= 6;
				}
			}
		}
	}
}


void topple4() {
	for (int r = 0; r < ARES; r++) {
		for (int c = 0; c < ARES; c++) {
			if (sand[r][c] >= 4) {
				int spillage = sand[r][c] / 50;

				if(r < ARES-1) sand[r + 1][c] += spillage;
				if(r > 0)      sand[r - 1][c] += spillage;
				if(c < ARES-1) sand[r][c + 1] += spillage;
				if(c > 0)      sand[r][c - 1] += spillage;

				sand[r][c] %= 61;
			}
		}
	}
}


void topple8() {
	for (int r = 0; r < ARES; r++) {
		for (int c = 0; c < ARES; c++) {
			if (sand[r][c] >= 8) {
				int spillage = sand[r][c] / 8;

				if (r < ARES-1 && c > 0)       sand[r+1][c-1] += spillage;
				if (r < ARES-1)                sand[r+1][c] += spillage;
				if (r < ARES-1 && c < ARES-1)  sand[r+1][c+1] += spillage;
				if (c > 0)                     sand[r][c-1] += spillage;
				if (c < ARES-1)                sand[r][c+1] += spillage;
				if (r > 0 && c > 0)            sand[r-1][c-1] += spillage;
				if (r > 0)                     sand[r-1][c] += spillage;
				if (r > 0 && c < ARES-1)       sand[r-1][c+1] += spillage;

				sand[r][c] %= 8;
			}
		}
	}
}


void fill3d(unsigned char arr[ARES][ARES][3]) {
	// puts a color at every array location
	for (int r = 0; r < ARES; r++) {
		for (int c = 0; c < ARES; c++) {
			switch (sand3d[r][c][ARES/2]) {
			case 0:
				arr[r][c][0] = 0;
				arr[r][c][1] = 0;
				arr[r][c][2] = 0;
				break;
			case 1:
				arr[r][c][0] = 255;
				arr[r][c][1] = 0;
				arr[r][c][2] = 0;
				break;
			case 2:
				arr[r][c][0] = 0;
				arr[r][c][1] = 255;
				arr[r][c][2] = 0;
				break;
			case 3:
				arr[r][c][0] = 0;
				arr[r][c][1] = 0;
				arr[r][c][2] = 255;
				break;
			case 4:
				arr[r][c][0] = 255;
				arr[r][c][1] = 255;
				arr[r][c][2] = 0;
				break;
			case 5:
				arr[r][c][0] = 255;
				arr[r][c][1] = 0;
				arr[r][c][2] = 255;
				break;
			default:
				arr[r][c][0] = 255;
				arr[r][c][1] = 255;
				arr[r][c][2] = 255;
				break;
			}
		}
	}
}


void fill4(unsigned char arr[ARES][ARES][3]) {
	// puts a color at every array location
	for(int r = 0; r < ARES; r++) {
		for(int c = 0; c < ARES; c++) {
			switch (sand[r][c]) {
			case 0:
				arr[r][c][0] = 0;
				arr[r][c][1] = 0;
				arr[r][c][2] = 0;
				break;
			case 1:
				arr[r][c][0] = 255;
				arr[r][c][1] = 0;
				arr[r][c][2] = 0;
				break;
			case 2:
				arr[r][c][0] = 0;
				arr[r][c][1] = 255;
				arr[r][c][2] = 0;
				break;
			case 3:
				arr[r][c][0] = 0;
				arr[r][c][1] = 0;
				arr[r][c][2] = 255;
				break;
			default:
				arr[r][c][0] = 255;
				arr[r][c][1] = 255;
				arr[r][c][2] = 255;
				break;
			}
		}
	}
}


void fill8(unsigned char arr[ARES][ARES][3]) {
	// puts a color at every array location
	for (int r = 0; r < ARES; r++) {
		for (int c = 0; c < ARES; c++) {
			switch (sand[r][c]) {
			case 0:
				arr[r][c][0] = 0;
				arr[r][c][1] = 0;
				arr[r][c][2] = 0;
				break;
			case 1:
				arr[r][c][0] = 255;
				arr[r][c][1] = 245;
				arr[r][c][2] = 0;
				break;
			case 2:
				arr[r][c][0] = 0;
				arr[r][c][1] = 255;
				arr[r][c][2] = 0;
				break;
			case 3:
				arr[r][c][0] = 165;
				arr[r][c][1] = 0;
				arr[r][c][2] = 255;
				break;
			case 4:
				arr[r][c][0] = 255;
				arr[r][c][1] = 255;
				arr[r][c][2] = 120;
				break;
			case 5:
				arr[r][c][0] = 255;
				arr[r][c][1] = 122;
				arr[r][c][2] = 255;
				break;
			case 6:
				arr[r][c][0] = 0;
				arr[r][c][1] = 255;
				arr[r][c][2] = 255;
				break;
			case 7:
				arr[r][c][0] = 128;
				arr[r][c][1] = 128;
				arr[r][c][2] = 128;
				break;
			default:
				arr[r][c][0] = 255;
				arr[r][c][1] = 255;
				arr[r][c][2] = 255;
				break;
			}
		}
	}
}

