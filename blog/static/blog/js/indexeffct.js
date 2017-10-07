/**
 * Created by jordan on 10/5/2017.
 */
function goTop() {
    $(window).scroll(function (e) {
        //若滚动条离顶部大于100元素
        if ($(window).scrollTop() > 400)
            $("#gotop").fadeIn(1000);//以1秒的间隔渐显id=gotop的元素
        else
            $("#gotop").fadeOut(1000);//以1秒的间隔渐隐id=gotop的元素
    });
};
$(function () {
    //点击回到顶部的元素
    $("#gotop").click(function (e) {
        //以1秒的间隔返回顶部
        $('body,html').animate({scrollTop: 0}, 1000);
    });
    $("#gotop").mouseout(function (e) {
        $(gotop).addClass()
    });
    goTop();//实现回到顶部元素的渐显与渐隐
});

$(function () {
    var ie6 = document.all;
    var dv = $('#textfloat'), st;
    dv.attr('otop', dv.offset().top); //存储原来的距离顶部的距离
    $(window).scroll(function () {
        st = Math.max(document.body.scrollTop || document.documentElement.scrollTop);
        if (st > parseInt(dv.attr('otop'))) {
            if (ie6) {//IE6不支持fixed属性，所以只能靠设置position为absolute和top实现此效果
                dv.css({position: 'absolute', top: st});
            }
            else if (dv.css('position') != 'fixed') dv.css({'position': 'fixed', top: 20});
        } else if (dv.css('position') != 'static') dv.css({'position': 'static'});
    });
});