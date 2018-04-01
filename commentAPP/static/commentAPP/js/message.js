window.onload=function (ev) {
  document.getElementById("id_text").innerText="";
};
function judge() {
    if(document.getElementById("id_text").value===""){
        alert("输入不能为空!");
        return false;
    }
}
function agree(p,pk) {
    p.childNodes[1].innerText=(Number(p.innerText)+1).toString();
    p.setAttribute("disabled","disabled");
    var xmlhttp;
    if(window.XMLHttpRequest){xmlhttp=new XMLHttpRequest();}
    else{xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");}
    xmlhttp.open("GET","../message_agree/"+pk.toString()+"/1/",true);
    xmlhttp.send();
}
function disagree(p,pk) {
    p.childNodes[1].innerText=(Number(p.innerText)+1).toString();
    p.setAttribute("disabled", "disabled");
    var xmlhttp;
    if(window.XMLHttpRequest){xmlhttp=new XMLHttpRequest();}
    else{xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");}
    xmlhttp.open("GET","../message_agree/"+pk.toString()+"/0/",true);
    xmlhttp.send();
}
function create(p,pk) {

    if(p.value==="0") {
        move_text();//删除所有已经生成的文本框,保证id唯一
        p.value = 1;
        var text = document.createElement("textarea");
        text.setAttribute("name", "reply");
        text.setAttribute("class", "form-control");
        text.setAttribute("rows", "3");
        text.setAttribute("cols", "20");
        text.setAttribute("placeholder", "输入你对这条留言的看法吧");
        text.setAttribute("maxlength", "500");
        text.required = "required";
        text.id="id_reply";
        var btn = document.createElement("button");
        btn.setAttribute("class", "btn btn-success btn-sm");
        btn.name="btn_create";
        btn.type = "button";
        btn.title = "submit";
        btn.innerText = "提交";
        btn.onclick = function (ev) {
            send(p,pk);
        };
        p.parentNode.appendChild(text);
        p.parentNode.appendChild(btn);
        text.focus();
    }else{
        p.value=0;
        move_text();//删除所有已经生成的文本框,保证id唯一
    }
}
function move_text() {
    var r=document.getElementsByName("reply");
    var b=document.getElementsByName("btn_create");
    for(var i=r.length-1;i>=0;--i){
        r[i].parentElement.firstElementChild.value=0;
        r[i].parentElement.removeChild(r[i]);
    }
    for(var j=b.length-1;j>=0;--j){
        b[j].parentNode.removeChild(b[j]);
    }
}
function send(p,pk) {
    var xmlhttp;
    var text=document.getElementById("id_reply");
    if(text.value===""){alert("评论不可以为空!");return 0;}
    if(window.XMLHttpRequest){
        xmlhttp=new XMLHttpRequest();
    }else{
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    var cs=document.getElementsByName("csrfmiddlewaretoken");
    var postdata=cs[0].name+"="+cs[0].value+"&"+text.name+"="+text.value+"&pk="+pk.toString();
    xmlhttp.open("POST", "../ftm/", true);
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.send(postdata);
    xmlhttp.onreadystatechange=function (e) {
        if(xmlhttp.readyState===4){
            if(xmlhttp.status !== 200){alert("评论失败!发生未知错误");return 0;}
            p.value=0;
            move_text();
            add_new(p,xmlhttp.responseText,text.value);
        }
    }
}
function add_new(p,hre,text) {
    var a=document.createElement("a");
    a.href=hre;
    a.innerText=document.getElementById("user").innerText;
    var time=document.createElement("small");
    time.innerText=gettime();
    time.style="float: right;vertical-align: bottom";
    var pp=document.createElement("p");
    pp.setAttribute("style","word-break: break-all");
    pp.appendChild(a);
    pp.innerHTML+=": "+text;
    pp.appendChild(time);
    var div=p.parentElement.parentElement.lastElementChild;
    div.appendChild(pp);
    div.appendChild(document.createElement("hr"));
}
function gettime() {
    var date=new Date();
    var timestr=date.getFullYear().toString()+"年"+(date.getMonth()+1).toString()+"月"+date.getDate().toString()+"日 ";
    if(date.getHours()===0){timestr+="00:";}
    else if(date.getHours()<10){timestr+="0"+date.getHours()+":";}
    else{timestr+=date.getHours()+":"}
    if(date.getMinutes()===0){timestr+="00";}
    else if(date.getMinutes()<10){timestr+="0"+date.getMinutes();}
    else{timestr+=date.getMinutes();}
    return timestr;
}