<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ChatLogin.aspx.cs" Inherits="ChatLogin" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
    <style type="text/css">
        .auto-style1 {
            width: 61%;
            height: 115px;
        }
        .auto-style2 {
            height: 20px;
            text-align: center;
        }
        .auto-style4 {
            width: 296px;
        }
        .auto-style5 {
            width: 280px;
            text-align: center;
        }
        .auto-style6 {
            width: 280px;
            height: 20px;
            text-align: center;
        }
        .auto-style7 {
            width: 296px;
            height: 20px;
        }
        .auto-style8 {
            width: 146px;
        }
        .auto-style9 {
            width: 146px;
            height: 20px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <table class="auto-style1">
            <tr>
                <td class="auto-style2" colspan="3">我的聊天室</td>
            </tr>
            <tr>
                <td class="auto-style5">用户名：</td>
                <td class="auto-style8">
                    <asp:TextBox ID="txtName" runat="server"></asp:TextBox>
                </td>
                <td class="auto-style4">
                    <asp:RequiredFieldValidator ID="rfvName" runat="server" ControlToValidate="txtName" ErrorMessage="RequiredFieldValidator">*</asp:RequiredFieldValidator>
                </td>
            </tr>
            <tr>
                <td class="auto-style6">密码：</td>
                <td class="auto-style9">
                    <asp:TextBox ID="txtPassword" runat="server" TextMode="Password"></asp:TextBox>
                </td>
                <td class="auto-style7">
                    <asp:RequiredFieldValidator ID="rfvPassword" runat="server" ControlToValidate="txtPassword" ErrorMessage="RequiredFieldValidator">*</asp:RequiredFieldValidator>
                </td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td colspan="2">
                    <asp:Button ID="btnLogin" runat="server" OnClick="btnLogin_Click" Text="登录" />
                </td>
            </tr>
        </table>
    <div>
    
    </div>
    </form>
</body>
</html>
