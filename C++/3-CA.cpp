#include <iostream>
#include <cmath>
#include <GL/freeglut_std.h>
using namespace std;


// consts
const int WRES = 768;
const int ARES = 256;


// functions
void display();
void fill(unsigned char arr[ARES][ARES][3]);
bool whichColor(int rule, bool A, bool B, bool C);
bool whichColor5(int rule, bool A, bool B, bool C, bool D, bool E);


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
	// init the top row of the array to 
	// have one white in the middle
	arr[ARES - 1][ARES / 2][0] = 255;
	arr[ARES - 1][ARES / 2][1] = 255;
	arr[ARES - 1][ARES / 2][2] = 255;

	// have random squares on and off
	for (int c = 0; c < ARES - 1; c++) {
		bool randBool = rand()%2;
		arr[ARES - 1][c][0] = randBool * 255;
		arr[ARES - 1][c][1] = randBool * 255;
		arr[ARES - 1][c][2] = randBool * 255;
	}

	// put a color at every array location
	for(int r = ARES-2; r >= 0; r--) {
		for(int c = 0; c < ARES; c++) {
			bool color = whichColor(106, //arr[r+1][(c-2+ARES)%ARES][0],
										arr[r + 1][(c - 1 + ARES) % ARES][0],
										arr[r + 1][c][0],
										arr[r + 1][(c + 1) % ARES][0]);
										//arr[r+1][(c+2)%ARES][0]);
			arr[r][c][0] = 255 * color; // red
			arr[r][c][1] = 255 * color; // green
			arr[r][c][2] = 255 * color; // blue
		}
	}
}


bool whichColor5(int rule, bool A, bool B, bool C, bool D, bool E) {
	return (1 << (A * 16 + B * 8 + C * 4 + D * 2 + E)) & rule;
}



bool whichColor(int rule, bool A, bool B, bool C) {
	return (1 << (A * 4 + B * 2 + C)) & rule;

	/*store the rule as a binary array
	bool binRule[8] = { 0 };
	for (int i = 0; i < 8; i++) {
		binRule[i] = (1 << i) & rule;
	}

	// convert A, B and C into an int to access binRule
	return binRule[A*4 + B*2 + C];

	//
	//return (A&&B&&C) || (A&&B&&!C) || (A&&!B&&!C) || (!A&&!B&&C);

	// check all 8 clauses, ORing together the true ones in the rule
	bool result = false;
	
	// compute our clause for A B and C
	for (int i = 7; i >= 0; i--) {
		if ((1 << i) & rule) {
			bool clause = true;
			clause &= (i >= 4) ? A : !A;
			clause &= (i%4 > 1) ? B : !B;
			clause &= (i%2==1) ? C : !C;
			result = result || clause;
		}
	}
	
	return result;
	*/
}