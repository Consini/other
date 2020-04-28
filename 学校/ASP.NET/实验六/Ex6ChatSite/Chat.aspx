<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Chat.aspx.cs" Inherits="Chat" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
    <script src="Scripts/jquery-3.5.0.min.js"></script>
    <%-- "refresh()函数以500ms为间隔，连续地局部刷新div层divMsg，其中$.ajax()调用jQuery提供的ajax()方法，用于执行异步请求 " --%>
    <script type="text/javascript">
        function refresh() {
            $.ajax({
                ur1: "Ajax.aspx",
                cache: false,
                success: function (text) {
                    document.getElementById("divMsg").innerHTML=text;
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    alert("网络连接有问题，请重试！");
                }
            })
            setTimeout("refresh()",500);
        }
    </script>
</head>
<body onload="fefresh()">
    <form id="form1" runat="server">
        <div id="divMsg">

            <br />

        </div>
    <div>
       
        <asp:Label ID="lblName" runat="server"></asp:Label>
       
    </div>
        <asp:TextBox ID="txtMsg" runat="server" Height="270px" TextMode="MultiLine" Width="482px"></asp:TextBox>
        <br />
        <asp:Button ID="btnSend" runat="server" Text="发送" OnClick="btnSend_Click" />
    </form>
</body>
</html>
