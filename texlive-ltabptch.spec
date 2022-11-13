Name:		texlive-ltabptch
Version:	17533
Release:	1
Summary:	Bug fix for longtable
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltabptch
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltabptch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltabptch.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A patch for LaTeX bugs tools/3180 and tools/3480. The patch
applies to version 4.11 of longtable.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ltabptch/ltabptch.sty
%doc %{_texmfdistdir}/doc/latex/ltabptch/README
%doc %{_texmfdistdir}/doc/latex/ltabptch/ltabptch.pdf
%doc %{_texmfdistdir}/doc/latex/ltabptch/ltabptch.tex
%doc %{_texmfdistdir}/doc/latex/ltabptch/ltabtest.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
