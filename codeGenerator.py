
initialCode = []
variables = {}
sineWave = ["void renderWave() {"]

def render(function):
    createInitialCode()

    if function == "SIN":
        renderWave()
    
def createInitialCode():
    defaultCode =   "Graph graph; \n" \
                    "PFont font; \n" \
                    "PVector pos; \n" \
                    "boolean locked = false; \n" \
                    "float xOffset = 0; \n" \
                    "float yOffset = 0; \n" \
                    "float ySineOffset = 550; \n" \
                    "float xSineOffset = 990; \n" \
                    "float scale = 1; \n" \

                    "int xspacing = 16;   // How far apart should each horizontal location be spaced \n" \
                    "int w;              // Width of entire wave \n" \

                    "float theta = 0.0;  // Start angle at 0 \n" \
                    "float amplitude = 75.0;  // Height of wave \n" \
                    "float period = 500.0;  // How many pixels before the wave repeats \n" \
                    "float dx;  // Value for incrementing X, a function of period and xspacing \n" \
                    "float[] yvalues;  // Using an array to store height values for the wave \n" \

                    "void setup() { \n" \

                    "fullScreen(); \n" \
                    "font = createFont("Consolas", 50); \n" \
                    "textFont(font, 15); \n" \
                    "pos = new PVector(width/2, height/2); \n" \
                    "textAlign(CENTER); \n" \
                    "graph = new Graph(-1, 0, 10); \n" \
                    "//rectMode(CENTER); \n" \
                    "strokeWeight(2); \n" \
                    "noFill(); \n" \
                    
                    "//SINEWAVE \n" \
                    "w = width+90; \n" \
                    "dx = (TWO_PI / period) * xspacing; \n" \
                    "yvalues = new float[w/xspacing]; \n" \
                    "//END_SINEWAVE \n" \
                    "} \n" \

                    "void mousePressed() { \n" \
                    "locked = true; \n" \
                    "xOffset = mouseX-pos.x;  \n" \
                    "yOffset = mouseY-pos.y; \n" \
                    "} \n" \

                    "void mouseDragged() { \n" \
                    "if (locked) { \n" \
                    "    pos.x = mouseX-xOffset;  \n" \
                    "    pos.y = mouseY-yOffset; \n" \
                    "} \n" \
                    "} \n" \

                    "void mouseReleased() { \n" \
                    "locked = false; \n" \
                    "} \n" \

                    "void draw() { \n" \
                    "background(0); \n" \
                    "translate(pos.x, pos.y); \n" \
                    "textSize(20); \n" \

                    "graph.displayGrid(); \n" \
                    
                    "calcWave(); \n" \
                    "renderWave(); \n" \
                    "} \n" \

                    "class Graph { \n" \
                    "ArrayList<PVector> points = new ArrayList<PVector>(); \n" \
                    "float[] variables = new float[3]; \n" \
                    "float increment = 0.1; //the smaller, the more accurate \n" \
                    "float range = 100; \n" \
                    "float graphincrement = 50; \n" \
                    "float scale = 10; //scaled down by 10 \n" \

                    "Graph(float a, float b, float c) { \n" \
                    "    variables[0] = a; \n" \
                    "    variables[1] = b; \n" \
                    "    variables[2] = c; \n" \

                    "    for (float i = -range; i < range+increment; i += increment) { \n" \
                    "    if ((i > -range*10) && (i < range*10)) { \n" \
                    "        PVector p = new PVector(i, equation(i)); \n" \
                    "        p.mult(scale); \n" \
                    "        points.add(p); \n" \
                    "    } \n" \
                    "    } \n" \
                    "} \n" \

                    "float equation(float n){ \n" \
                    "    //put equation here \n" \
                    "    return -variables[0]*pow(n, 2) - variables[1]*n - variables[2]; \n" \
                        
                    "} \n" \

                    "void displayGrid() { \n" \
                    "    textSize(15); \n" \
                    "    for (float x = -range*10; x < range*10+graphincrement; x += graphincrement) { \n" \
                    "    if (x == 0) { \n" \
                    "        strokeWeight(5); \n" \
                    "        stroke(255, 200); \n" \
                    "    } else { \n" \
                    "        strokeWeight(2); \n" \
                    "        stroke(255, 100); \n" \
                    "    } \n" \
                    "    line(x, -range*10, x, range*10); \n" \
                    "    text(round(x/scale), x, -15); \n" \
                    "    } \n" \
                    "    for (float y = -range*10; y < range*10+graphincrement; y += graphincrement) { \n" \
                    "    if (y == 0) { \n" \
                    "        strokeWeight(5); \n" \
                    "        stroke(255, 200); \n" \
                    "    } else { \n" \
                    "        strokeWeight(2); \n" \
                    "        stroke(255, 100); \n" \
                    "    } \n" \
                    "    line(-range*10, y, range*10, y); \n" \
                    "    text(round(-y/scale), -15, y); \n" \
                    "    } \n" \
                    "} \n" \
                    "} \n" \

                    "void calcWave() { \n" \
                    "// Increment theta (try different values for 'angular velocity' here \n" \
                    "theta += 0.02; \n" \

                    "// For every x value, calculate a y value with sine function \n" \
                    "float x = theta; \n" \
                    "for (int i = 0; i < yvalues.length; i++) { \n" \
                    "    yvalues[i] = sin(x)*amplitude; \n" \
                    "    x+=dx; \n" \
                    "} \n" \
                    "} \n" 

    initialCode.append(defaultCode)

def renderWave():
     sinewaveCode = "void renderWave() { \n" \
                    "noStroke(); \n" \
                    "fill(255); \n" \
                    "// A simple way to draw the wave with an ellipse at each location \n" \
                    "for (int x = 0; x < yvalues.length; x++) { \n" \
                    "ellipse(x*xspacing-xSineOffset, height/2+yvalues[x] - ySineOffset, 16, 16); \n" \
                    "} \n" \
                    "} \n" 
def upload():
    finalCode = initialCode[0]

    finalCode += sinewaveCode
    finalCode += "}"

    filePath = "PPP.pde"
    ProcessingCode = open(filePath, 'w')
    ProcessingCode.write(finalCode)
    ProcessingCode.close()