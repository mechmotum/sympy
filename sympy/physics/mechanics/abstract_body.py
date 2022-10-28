from abc import ABC, abstractmethod

from sympy.core.backend import Symbol, sympify
from sympy.physics.vector import Point

__all__ = ['_Body']


class _Body(ABC):
    """Abstract class for body type objects."""
    def __init__(self, name, masscenter=None, mass=None):
        if not isinstance(name, str):
            raise TypeError('Supply a valid name.')
        self._name = name
        if mass is None:
            mass = Symbol(f'{name}_mass')
        if masscenter is None:
            masscenter = Point(f'{name}_masscenter')
        self.mass = mass
        self.masscenter = masscenter
        self.potential_energy = 0
        self.points = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    @property
    def name(self):
        return self._name

    @property
    @abstractmethod
    def frame(self):
        """The ReferenceFrame fixed to the body."""
        pass

    @frame.setter
    @abstractmethod
    def frame(self, frame):
        pass

    @property
    def masscenter(self):
        """The body's center of mass."""
        return self._masscenter

    @masscenter.setter
    def masscenter(self, point):
        if not isinstance(point, Point):
            raise TypeError("The body's center of mass must be a Point object.")
        self._masscenter = point

    @property
    def mass(self):
        """The body's mass."""
        return self._mass

    @mass.setter
    def mass(self, mass):
        self._mass = sympify(mass)

    @property
    def x(self):
        """The basis Vector for the Body, in the x direction. """
        return self.frame.x

    @property
    def y(self):
        """The basis Vector for the Body, in the y direction. """
        return self.frame.y

    @property
    def z(self):
        """The basis Vector for the Body, in the z direction. """
        return self.frame.z

    @property
    def potential_energy(self):
        """The potential energy of the Particle.

        Examples
        ========

        >>> from sympy.physics.mechanics import Particle, Point
        >>> from sympy import symbols
        >>> m, g, h = symbols('m g h')
        >>> O = Point('O')
        >>> P = Particle('P', O, m)
        >>> P.potential_energy = m * g * h
        >>> P.potential_energy
        g*h*m

        """
        return self._potential_energy

    @potential_energy.setter
    def potential_energy(self, scalar):
        """Used to set the potential energy of the Particle.

        Parameters
        ==========

        scalar : Sympifyable
            The potential energy (a scalar) of the Particle.

        Examples
        ========

        >>> from sympy.physics.mechanics import Particle, Point
        >>> from sympy import symbols
        >>> m, g, h = symbols('m g h')
        >>> O = Point('O')
        >>> P = Particle('P', O, m)
        >>> P.potential_energy = m * g * h

        """
        self._potential_energy = sympify(scalar)

    @abstractmethod
    def kinetic_energy(self, frame):
        pass

    @abstractmethod
    def linear_momentum(self, frame):
        pass

    @abstractmethod
    def angular_momentum(self, point, frame):
        pass

    @abstractmethod
    def parallel_axis(self, point, frame):
        pass
