function search_judge() {
    var text=document.getElementById("search_in");
    if (text.value.length===0) {
        alert("请输入关键词后再查询!");
        return false;
    }
}
function change(se) {
    var form=document.getElementById("search_out_form");
    var text=document.getElementById("search_out");
    if(se.value==='google'){
        form.action="https://www.google.com.hk/search";
        text.name="q";
        se.parentElement.parentElement.parentElement.style.backgroundImage="url('/static/resourcesAPP/img/gg_logo.png')";
    } else {
        form.action="https://www.baidu.com/s";
        text.name="wd";
        se.parentElement.parentElement.parentElement.style.backgroundImage="url('/static/resourcesAPP/img/bd_logo.png')";
    }
}


//details 的评论部分:
function agree(btn,pk,flag) {
    var xmlhttp,url;
    if(flag==="1"){url="../../../comment/father_agree/"+pk.toString()+"/1/";}
    else {url="../../../comment/son_agree/"+pk.toString()+"/1/";}
    if(window.XMLHttpRequest){xmlhttp=new XMLHttpRequest();}
    else {xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");}
    xmlhttp.open("GET",url,true);
    xmlhttp.send();
    btn.firstChild.innerText=(Number(btn.firstChild.innerText)+1).toString();
    btn.disabled="disabled";
}
function disagree(btn,pk,flag) {
    var url,xmlhttp;
    if(flag==="1"){url="../../../comment/father_agree/"+pk.toString()+"/0/";}
    else {url="../../../comment/son_agree/"+pk.toString()+"/0/";}
    if(window.XMLHttpRequest){xmlhttp=new XMLHttpRequest();}
    else {xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");}
    xmlhttp.open("GET",url,true);
    xmlhttp.send();
    btn.firstChild.innerText=(Number(btn.firstChild.innerText)+1).toString();
    btn.disabled="disabled";
}
function send_father(pk) {//发送一级评论
    var text=document.getElementById("reply");
    if(text.value.length===0){alert("评论不能为空!");return ;}
    var xmlhttp;
    if(window.XMLHttpRequest){
        xmlhttp=new XMLHttpRequest();
    }else{
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    var cs=document.getElementsByName("csrfmiddlewaretoken")[0];
    var postdata=cs.name+"="+cs.value+'&'+text.name+"="+text.value+"&pk="+pk.toString();
    xmlhttp.open("POST","../../../comment/fta/",true);
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.send(postdata);
    xmlhttp.onreadystatechange=function () {
        if(xmlhttp.readyState===4){
            if(xmlhttp.status===200){
                add_new_father(text.value, xmlhttp.responseText);
                text.value="";
            }else{alert(xmlhttp.responseText);}
        }
    }
}
function create_father_text(btn,pk) {//创造回复一级评论的文本框
    if(btn.value==="0"){
        remove_created();//删除所有创建出来的评论框,保证id唯一
        btn.value=1;
        var div=btn.parentElement;
        var text=document.createElement("textarea");
        text.setAttribute("name", "reply");
        text.setAttribute("class", "form-control");
        text.setAttribute("rows", "3");
        text.setAttribute("cols", "20");
        text.setAttribute("placeholder", "输入你的看法吧");
        text.setAttribute("maxlength", "500");
        text.required = true;
        text.setAttribute("id","reply_father");
        var sub=document.createElement("button");
        sub.setAttribute("class", "btn btn-success btn-sm");
        sub.type = "button";
        sub.title = "submit";
        sub.innerText = "提交";
        sub.onclick = function () {
                send_son_to_father(btn,pk);
            };
        var fa=document.createElement("div");
        fa.setAttribute("name","created");
        fa.className="text-right";
        fa.appendChild(text);
        fa.appendChild(sub);
        div.appendChild(fa);
        text.focus();
    }else{
        btn.value=0;
        remove_created();//删除所有创建出来的评论框,保证id唯一
    }
}
function remove_created() {
    var de=document.getElementsByName("created");
    for(var i=de.length-1;i>=0;--i){
        de[i].parentElement.firstElementChild.value="0";
        de[i].parentElement.removeChild(de[i]);
    }
}
function send_son_to_father(btn,pk){
 //第一个是所属的按钮btn,发送后在这个下面创建
//pk 是所属的一级评论 而且是要回复的一级评论
    var text=document.getElementById("reply_father");
    if(text.value===""){alert("评论不能为空!");return;}
    var xmlhttp;
    if(window.XMLHttpRequest){
        xmlhttp=new XMLHttpRequest();
    }else{xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");}
    var cs=document.getElementsByName("csrfmiddlewaretoken")[0];
    var postdata=cs.name+"="+cs.value+"&"+text.name+"="+text.value+"&pk="+pk.toString();
    xmlhttp.open("POST","../../../comment/stf/",true);
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.send(postdata);
    xmlhttp.onreadystatechange=function () {
        if(xmlhttp.readyState===4){
            if(xmlhttp.status===200){
                add_new_son(btn,text.value);
                remove_created();
            }else{alert(xmlhttp.responseText);}
        }
    }
}
function create_son_text(btn,pk,pkk) {
    if(btn.value==="0"){
        remove_created();//删除所有,保证id唯一
        btn.value=1;
        var div=btn.parentElement;
        var text=document.createElement("textarea");
        text.setAttribute("name", "reply");
        text.setAttribute("class", "form-control");
        text.setAttribute("rows", "3");
        text.setAttribute("cols", "16");
        text.setAttribute("placeholder", "输入你的看法吧");
        text.setAttribute("maxlength", "500");
        text.required = true;
        text.setAttribute("id","reply_son");
        var sub=document.createElement("button");
        sub.setAttribute("class", "btn btn-success btn-sm");
        sub.type = "button";
        sub.innerText = "提交";
        sub.onclick = function () {
            send_son_to_son(btn,pk,pkk);
            };
        var fa=document.createElement("div");
        fa.setAttribute("name","created");
        fa.className="text-right";
        fa.appendChild(text);
        fa.appendChild(sub);
        div.appendChild(fa);
        text.focus();
    }else{
        remove_created();//删除所有的
    }
}
function send_son_to_son(btn,pk,pkk) {
//btn是按钮 pk是所属的一级评论,pkk是将要回复的二级评论
    var text=document.getElementById("reply_son");
    if(text.value===""){alert("评论不能为空!");return;}
    var xmlhttp;
    if(window.XMLHttpRequest){
        xmlhttp=new XMLHttpRequest();
    }else{xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");}
    var cs=document.getElementsByName("csrfmiddlewaretoken")[0];
    var postdata=cs.name+"="+cs.value+"&"+text.name+"="+text.value+"&pk="+pk.toString()+"&pkk="+pkk.toString();
    xmlhttp.open("POST","../../../comment/sts/",true);
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.send(postdata);
    xmlhttp.onreadystatechange=function () {
        if(xmlhttp.readyState===4){
            if(xmlhttp.status===200){
                add_son_to_son(btn,text.value);
                remove_created();
            }else{alert(xmlhttp.responseText);}
        }
    }
}
//发送评论后在网页上创建评论结果

//增加回复一级评论的二级评论
function add_new_son(btn,text) {
    var fa=btn.parentElement.parentElement.lastElementChild;
    var small=document.createElement("small");
    var afrom=document.getElementById("username");
    var ato=btn.parentElement.parentElement.parentElement.firstElementChild.firstElementChild;
    small.innerHTML='<a href=\"'+afrom.href+'\"> @'+afrom.innerText+'</a> 回复: <a href=\"'+ato.href+'\">@'+ato.innerText+'</a>';
    var span=document.createElement("span");
    span.style.wordBreak ="break-all";
    span.innerText=text;
    var div=document.createElement("div");
    div.style.backgroundColor="#eeeeee";
    var time_div=document.createElement("div");
    var time=document.createElement("small");
    time_div.setAttribute("class","col text-right");
    time.innerText=gettime();
    time_div.appendChild(time);
    div.appendChild(small);
    div.appendChild(span);
    div.appendChild(time_div);
    var hr=document.createElement("hr");
    hr.style.margin="1px";
    fa.insertBefore(hr,fa.firstElementChild);
    fa.insertBefore(div,fa.firstElementChild);
}
//增加回复二级评论的二级评论
function add_son_to_son(btn,text) {
    var fa=btn.parentElement.parentElement.parentElement;
    var small=document.createElement("small");
    var afrom=document.getElementById("username");
    var ato=btn.parentElement.parentElement.firstElementChild.firstElementChild;
    small.innerHTML='<a href=\"'+afrom.href+'\"> @'+afrom.innerText+'</a> 回复: <a href=\"'+ato.href+'\">'+ato.innerText+'</a>';
    var span=document.createElement("span");
    span.style.wordBreak ="break-all";
    span.innerText=text;
    var div=document.createElement("div");
    div.style.backgroundColor="#eeeeee";
    var time_div=document.createElement("div");
    var time=document.createElement("small");
    time_div.setAttribute("class","col text-right");
    time.innerText=gettime();
    time_div.appendChild(time);
    div.appendChild(small);
    div.appendChild(span);
    div.appendChild(time_div);
    var hr=document.createElement("hr");
    hr.style.margin="1px";
    fa.insertBefore(hr,fa.firstElementChild);
    fa.insertBefore(div,fa.firstElementChild);
}
//增加一级评论
function add_new_father(text, img_url) {
    var start=document.getElementById("comment_start");
    var div=document.createElement("div");
    div.className="row";
    div.style.border= "#00aa00 solid 1px";
    div.style.marginBottom="8px";
    var left=document.createElement("div");
    var right=document.createElement("div");
    left.className="col-2 text-center";
    left.style.borderRight=" #d01040 dotted 1px";
    left.style.paddingTop="4px";
    var a=document.getElementById("username");
    left.innerHTML='<a href=/"'+a.href+'><img class="img-fluid rounded-circle" src=\"'+img_url+'\">'+a.innerText+'</a><br/><small>贡献数:'+a.title+'</small>';
    right.className="col-10";
    right.appendChild(document.createElement("br"));
    var p=document.createElement("p");
    p.style.wordBreak="break-all";
    p.innerText=text;
    right.appendChild(p);
    right.appendChild(document.createElement("br"));
    right.appendChild(document.createElement("hr"));
    div.appendChild(left);
    div.appendChild(right);
    start.parentElement.insertBefore(div,start);
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
