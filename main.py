from cmu_graphics import *

GRID_SIZE = 28
MENU_ITEMS = ['Level Select', 'Instructions', 'Settings']

def onAppStart(app):
    app.width = 960
    app.height = 540
    app.hovered = None

def home_redrawAll(app):
    drawRect(0, 0, app.width, app.height,
             fill=gradient('white', rgb(245, 245, 245), start='top'))

    for x in range(0, app.width, GRID_SIZE):
        drawLine(x, 0, x, app.height, fill=rgb(0, 0, 0), opacity=8)
    for y in range(0, app.height, GRID_SIZE):
        drawLine(0, y, app.width, y, fill=rgb(0, 0, 0), opacity=8)

    drawLine(app.width * 0.38, app.height * 0.1,
             app.width * 0.38, app.height * 0.9,
             fill=rgb(180, 180, 180))

    drawLabel('RIDM', app.width * 0.19, app.height * 0.42,
              size=72, bold=True, font='monospace')
    drawLabel('By: Saathvik', app.width * 0.19, app.height * 0.58,
              size=14, fill='dimGray', font='monospace')

    menuX = app.width * 0.68
    menuY = app.height * 0.28
    menuSpacing = app.height * 0.22

    for i in range(len(MENU_ITEMS)):
        item = MENU_ITEMS[i]
        y = menuY + i * menuSpacing

        if app.hovered == i:
            color = 'dimGray'
        else:
            color = 'black'

        drawLine(app.width * 0.42, y + menuSpacing * 0.5,
                 app.width * 0.95, y + menuSpacing * 0.5,
                 fill=rgb(200, 200, 200))

        drawLabel(item, menuX, y + menuSpacing * 0.25,
                  size=28, bold=True, font='monospace',
                  fill=color, align='left')

def mouseInMenuItem(app, mouseX, mouseY, i):
    menuY = app.height * 0.28
    menuSpacing = app.height * 0.22
    menuLeft = app.width * 0.42
    menuRight = app.width * 0.95
    y = menuY + i * menuSpacing
    return (menuLeft <= mouseX <= menuRight) and (y <= mouseY <= y + menuSpacing)

def home_onMouseMove(app, mouseX, mouseY):
    app.hovered = None
    for i in range(len(MENU_ITEMS)):
        if mouseInMenuItem(app, mouseX, mouseY, i):
            app.hovered = i

def home_onMousePress(app, mouseX, mouseY):
    if app.hovered == 0:
        setActiveScreen('levelSelect')
    elif app.hovered == 1:
        setActiveScreen('instructions')
    elif app.hovered == 2:
        setActiveScreen('settings')

def main():
    runAppWithScreens(initialScreen='home')

main()