(function(){

	var canvas = document.getElementById( 'animation' ),
		c = canvas.getContext( '2d' ),
		i = 0,
		rowOne = [],
		rowTwo = [],
		rowThree = [],
		length = canvas.width * 0.4,
		origin = [ canvas.width / 2, canvas.height / 2 ],
		angle = 90,
		loop;

	function Circle( args ) {
		this.position  = [ 0, 0 ];
		this.angle     = 30;
		this.speed     = 1;
		this.offset    = 1;
		this.length    = 100;
		this.size      = 5;
		this.color     = '#fff';
		this.direction = 'grow';

		if ( 'undefined' !== typeof args.position )
			this.position = args.position;
		if ( 'undefined' !== typeof args.angle )
			this.angle = args.angle;
		if ( 'undefined' !== typeof args.speed )
			this.speed = args.speed;
		if ( 'undefined' !== typeof args.length )
			this.length = args.length;
		if ( 'undefined' !== typeof args.size )
			this.size = args.size;
		if ( 'undefined' !== typeof args.color )
			this.color = args.color;
		if ( 'undefined' !== typeof args.offset ) {
			this.offset = args.offset;
			this.length = canvas.width * this.offset * 0.03
		}
	}

	Circle.prototype.render = function() {
		this.move();
		this.draw();
	}

	Circle.prototype.draw = function() {
		c.fillStyle = this.color;
		c.beginPath();
		c.arc( this.position[0], this.position[1], ( this.size / 2 ), 0, Math.PI * 2, true );
		c.closePath();
		c.fill();
	}

	Circle.prototype.move = function() {
		this.angle = ( this.angle < 360 ) ? this.angle + this.speed : 0;

		if ( 'grow' == this.direction ) {
			this.length++;
			this.direction = ( 150 >= this.length ) ? 'grow' : 'shrink';
		} else {
			this.length--;
			this.direction = ( 50 <= this.length ) ? 'shrink' : 'grow';
		}

		this.position[0] = this.length * Math.sin( this.angle * ( Math.PI / 180 ) );
		this.position[1] = this.length * Math.cos( this.angle * ( Math.PI / 180 ) );

		this.position[0] = this.position[0] + origin[0];
		this.position[1] = this.position[1] + origin[1];
	}

	for ( i = 1; i < 10; i++ ) {
		var offset = 1;
		rowOne.push( new Circle( {
			angle: 0,
			offset: i
		} ) );
		rowTwo.push( new Circle( {
			angle: 120,
			offset: i
		} ) );
		rowThree.push( new Circle( {
			angle: 240,
			offset: i
		} ) );
	}

	function render() {
		c.fillStyle = 'rgba( 0, 0, 0, 0.025 )';
		c.fillRect( 0, 0, canvas.width, canvas.height );
		for ( i = 0; i < 9; i++ ) {
			rowOne[i].render();
			rowTwo[i].render();
			rowThree[i].render();
		}
	}

	(function animate() {
		render();
		loop = setTimeout( animate, 50 );
	})();

})();