function loginVerity() {

    let name = $('#name').val();
    let password = $('#password').val();

    $.ajax({
        url: "/user/login",
        type: "post",
        data: {
            "username": name,
            "password": password,
        },
        dataType: "json",
        success: function (result) {
            if(result.code === 200) {
                layer.msg(result.msg, {
                    time: 2000,
                    icon: 1
                });
                setTimeout(() => {
                    window.location = '/user/index';
                }, 2000)

            } else if(result.code === 404) {
                layer.msg(result.msg, {
                    time: 2000,
                    icon: 2
                });
            }
        }
    })
}

$("#loginBtn").click(function () {
    layer.open({
        type: 1
        ,title: "登录验证"
        ,closeBtn: false
        ,area: '400px;'
        ,shade: 0.8
        ,id: 'LAY_layuipro_login' //设定一个id，防止重复弹出
        ,btn: ['火速登录', '残忍拒绝']
        ,btnAlign: 'c'
        ,moveType: 1 //拖拽模式，0或者1
        ,content: $("#loginDemo").html()
        ,success: function(layero){
            var btn = layero.find('.layui-layer-btn');
            btn.find('.layui-layer-btn0').click(function () {
                loginVerity()
            })
        }
    });
});

function registerVerity() {
    let name = $('#rname').val();
    let password = $('#rpassword').val();
    let cpassword = $('#cpassword').val();
    let email = $('#remail').val();
    let phone = $('#rphone').val();

    $.ajax({
        url: "/user/register",
        data: {
            "username": name,
            "password": password,
            "cpassword": cpassword,
            "email": email,
            'phone': phone
        },
        type: "post",
        dataType: "json",
        success: function (result) {
            if(result.code === 200) {
                layer.msg(result.msg, {
                    time: 2000,
                    icon: 1
                })
            } else {
                layer.msg(result.msg, {
                    time: 2000,
                    icon: 2
                })
            }
        }
    })
}

$("#registerBtn").click(function () {
    layer.open({
        type: 1
        ,title: "注册用户"
        ,closeBtn: false
        ,area: '400px;'
        ,shade: 0.8
        ,id: 'LAY_layuipro_login' //设定一个id，防止重复弹出
        ,btn: ['火速注册', '残忍拒绝']
        ,btnAlign: 'c'
        ,moveType: 1 //拖拽模式，0或者1
        ,content: $("#registerDemo").html()
        ,success: function(layero){
            var btn = layero.find('.layui-layer-btn');
            btn.find('.layui-layer-btn0').click(function () {
                registerVerity();
            })
        }
    });
});

$("#clickBtn").click(()=>{
    let aid = $("#aid").val();
    $.ajax({
        url: "/article/click_add/"+aid,
        type: "get",
        success: function (result) {
            if(result.status === 200) {
                $("#click_time").text(parseInt($("#click_time").text()) + 1);
       }
        }
    })
});