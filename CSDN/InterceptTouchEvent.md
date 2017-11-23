## onInterceptTouchEvent(MotionEvent ev)

这是一个 ViewGroup 的方法，用于拦截点击事件。
> 当返回值为 true 的时候，拦截子 View 的点击事件

> 当返回值为 false 的时候，不拦截子 View 的点击事件

默认情况下返回 false。
<p>
一般应用情景，
</p>

<p>
当产生点击事件时，先调用 onInterceptTouchEvent() 方法，然后再调用 onTouchEvent() 方法。
</p>


## onTouchEvent()





