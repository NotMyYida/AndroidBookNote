##从一款鸭子游戏开始

超类（SuperClass）：

Class Duck{

	quack();	//所有鸭子都会呱呱叫

	swim();		//会游泳

	display();	//外观
}

子类：

Class MallardDuck{

	……
	
	display(){

	//外观是绿头
	
	}
}


Class RedHeadDuck{

	……
	display(){

	//外观是红头
	
	}
}


Class RubberDuck{

	……
	quack(){
	
	//覆盖成吱吱叫

	}

	display(){

	//外观是橡皮鸭
	
	}
}


结构是很不错的，程序员们过着幸福的日子。直到有一天，Boss决定加一个功能，