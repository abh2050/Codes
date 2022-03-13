#include <freeglut.h>
#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
using namespace std;


// consts
const int WRES = 800;
const int ARES = 800;
const int LEN = 255;
const double PI = 3.14159265359;
const double PHI = 1.61803398875;


// struct
struct Point {
	int x;
	int y;
	unsigned char r;
	unsigned char g;
	unsigned char b;
};


// functions
void display();
void fill(unsigned char arr[ARES][ARES][3], Point points[LEN]);
void init(Point points[LEN]);
int nearest(int r, int c, Point points[LEN]);
double distance(int x1, int y1, int x2, int y2);


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

	// set up array of points
	Point points[LEN];
	init(points);

	// make and fill in array
	static unsigned char arr[ARES][ARES][3] = {0};
	fill(arr, points);

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


void init(Point points[LEN]) {
	// init each point in the array
	for (int i = 0; i < LEN; i++) {
		// set the point's positions
		// x=rcos(theta) + offset, y=rsin(theta) + offset
		points[i].x = 20 * sqrt(i + 1) * cos(i*PI*PHI*2) + ARES/2;
		points[i].y = 20 * sqrt(i + 1) * sin(i*PI*PHI*2) + ARES/2;

		// set the point's colors
		points[i].r = i % 256;
		points[i].g = (2*i) % 256;
		points[i].b = (3*i) % 256;
	}
}


double distance(int x1, int y1, int x2, int y2) {
	return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
}


int nearest(int r, int c, Point points[LEN]) {
	int minIndex = 0;
	double minDistance = distance(c, r, points[0].x, points[0].y);

	// loop through all points
	for (int i = 0; i < LEN; i++) {
		double currentDistance = distance(c, r, points[i].x, points[i].y);
		// dist to current point is less than minDistance
		if (currentDistance < minDistance) {
			minDistance = currentDistance;
			minIndex = i;
		}
	}
	return minIndex;
}


void fill(unsigned char arr[ARES][ARES][3], Point points[LEN]) {
	for (int r = 0; r < ARES; r++) {
		for (int c = 0; c < ARES; c++) {
			// find the nearest point in the points array
			int index = nearest(r, c, points);

			// color it that same color
			arr[r][c][0] = points[index].r;
			arr[r][c][1] = points[index].g;
			arr[r][c][2] = points[index].b;
		}
	}
}

