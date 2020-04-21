﻿<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Calculator.aspx.cs" Inherits="ExSite4.Calculator" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div style="text-align: center">
    
    &nbsp;&nbsp;&nbsp; 简易计算器<br />
        <asp:TextBox ID="txtDisplay" runat="server" ReadOnly="True" Width="110px"></asp:TextBox>
        <br />
        <asp:Button ID="btnOne" runat="server" OnClick="btnOne_Click" Text="1" Width="40px" />
        <asp:Button ID="btnTwo" runat="server" OnClick="btnTwo_Click" Text="2" Width="40px" />
        <asp:Button ID="btnThree" runat="server" OnClick="btnThree_Click" Text="3" Width="40px" />
        <br />
        <asp:Button ID="btnAdd" runat="server" OnClick="btnAdd_Click" Text="+" Width="40px" />
        <asp:Button ID="btnSubtract" runat="server" OnClick="btnSubtract_Click" Text="-" Width="40px" />
        <asp:Button ID="btnEqual" runat="server" OnClick="btnEqual_Click" Text="=" Width="40px" />
    
    </div>
    </form>
</body>
</html>
