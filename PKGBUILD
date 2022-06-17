# Maintainer: Ajith <ajithar204@gmail.com>
pkgname=aurh
pkgver=0.0.1dev1
pkgrel=1
pkgdesc='Arch User Repository (AUR) Helper'
arch=('any')
url='https://github.com/ajthr/aurh.git'
license=('MIT')
depends=('python' 'python-click' 'pyalpm>=0.5.1-1' 'python-requests' 'python-srcinfo' 'git')
makedepends=('python-setuptools') 
changelog=CHANGELOG.txt
source=("https://files.pythonhosted.org/packages/source/${pkgname:0:1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
md5sums=('21de0e20c1f5f32a95973405b1a304af')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}"
    python setup.py build
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
    python setup.py install --root "${pkgdir}" --optimize=1
    install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
