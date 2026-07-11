%global tl_name ltabptch
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.74d
Release:	%{tl_revision}.1
Summary:	Bug fix for longtable
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ltabptch
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltabptch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltabptch.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A patch for LaTeX bugs tools/3180 and tools/3480. The patch applies to
version 4.11 of longtable.

