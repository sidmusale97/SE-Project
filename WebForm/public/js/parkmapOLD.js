var SVG = class{
    constructor(){}
    initialize(svg){
        this.svg = null;
        this.svgNS = "http://www.w3.org/2000/svg";
    }
    drawRectangle(id, x, y, w, h, fill, stroke, stroke_width) {
        var myRect = document.createElementNS(this.svgNS, "rect");
        myRect.setAttributeNS(null, "id", id);
        myRect.setAttributeNS(null, "x", x);
        myRect.setAttributeNS(null, "y", y);
        myRect.setAttributeNS(null, "width", w);
        myRect.setAttributeNS(null, "height", h);
        myRect.setAttributeNS(null, "fill", fill);
        myRect.setAttributeNS(null, "stroke", stroke);
        myRect.setAttributeNS(null, "stroke-width", stroke_width);
        document.body.appendChild(myRect);
        //this.svg.appendChild(myRect);
        return myRect;
    }
    drawLine(id, x1, y1, x2, y2, stroke, stroke_width) {
        var myLine = document.createElementNS(this.svgNS, "line");
        myLine.setAttributeNS(null, "id", id);
        myLine.setAttributeNS(null, "x1", x1);
        myLine.setAttributeNS(null, "y1", y1);
        myLine.setAttributeNS(null, "x2", x2);
        myLine.setAttributeNS(null, "y2", y2);
        myLine.setAttributeNS(null, "stroke", stroke);
        myLine.setAttributeNS(null, "stroke-width", stroke_width);
        this.svg.appendChild(myLine);
        return myLine;
    }
};

var parkingMap = {};
parkingMap.marker = null;

/*
Handler invoked when opening indoorMap on selected marker(Parking slot) which creates the SVG component
for indoor map only once and updates the slots from availabity status
*/


parkingMap.displayIndoorMap = function() {
    var mapMarker = parkingMap.marker;
    if (!parkingMap.mySvg) {
        parkingMap.rectArray = [];
        parkingMap.lineArray = [];
        parkingMap.mySvg = new SVG(document.getElementById('mapGraphic'));
        for (var i = 0; i < 5; i++) {
            parkingMap.rectArray.push(this.mySvg.drawRectangle("id" + i, 700+(48*i), 38 + i, 48, 96, "red", "none", 0));
           // parkingMap.rectArray.push(this.mySvg.drawRectangle("col" + 5 + "r" + i, 459, 71 + i * 20, 39, 18, "red", "none", 0));
        }
        for (var i = 0; i < 13; i++) {
            parkingMap.rectArray.push(this.mySvg.drawRectangle("col" + 1 + "r" + i, 139, 141 + i * 20, 39, 18, "red", "none", 0));
            parkingMap.rectArray.push(this.mySvg.drawRectangle("col" + 2 + "r" + i, 182, 141 + i * 20, 39, 18, "red", "none", 0));
            parkingMap.rectArray.push(this.mySvg.drawRectangle("col" + 3 + "r" + i, 299, 141 + i * 20, 39, 18, "red", "none", 0));
            parkingMap.rectArray.push(this.mySvg.drawRectangle("col" + 4 + "r" + i, 342, 141 + i * 20, 39, 18, "red", "none", 0));
        }
    }
    svg_10.style.fill='yellow'
    alert('test');
    //mapMarker.updateIndoorMap();
};

parkingMap.flushRects = function() {
    if (parkingMap.rectArray) {
        for (var i = 0; i < parkingMap.rectArray.length; i++) {
            $(parkingMap.rectArray[i]).css({
                fill: 'red'
            });
        };
    }
};

var Marker = {};
Marker = function() {
    this._marker = null;
    this._isIndoorMapOpen = false;
    this.availabilityCallback = function(item, status) {
        if (status === "ok") {
            this._item = item;
            this.setAvail(item.avail);
            this.setTotal(item.total);
            this.setAvailability();
            //update the indoor map only if opened
            if (this._isIndoorMapOpen) {
                this.updateIndoorMap();
            }
        }
    }
    this.updateIndoorMap = function() {
        parkingMap.flushRects();
        var r, c;
        for (var i in this._item.parkmap) {
            var r = parseInt(i.substr(1));
            if (r <= 18) c = 0;
            else if (r > 18 && r <= 31) {
                r = r - 19;
                c = 1;
            } else if (r > 31 && r <= 44) {
                r = r - 32;
                c = 2;
            } else if (r > 44 && r <= 57) {
                r = r - 45;
                c = 3;
            } else if (r > 57 && r <= 70) {
                r = r - 58;
                c = 4;
            } else if (r > 70) {
                r = r - 71;
                c = 5;
            }
            if (this._item.parkmap[i] == 1) {
                $("#col" + c + "r" + r).css({
                    fill: 'green'
                });
            } else {
                $("#col" + c + "r" + r).css({
                    fill: 'red'
                });
            }
        }
    };
}

testFunc = function(){
    alert('hello');
}