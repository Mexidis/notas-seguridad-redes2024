from fractions import Fraction
from Crypto.Util.number import inverse

# Valores proporcionados
c = 51196739434454963497826788439095104608116134410589770981149944066035377441539897180707754821043842358317065627826691085749649399697153729892415515154145953321253798025749281380203406803487743323823559769344327957866250238134085085574588235281979870355787492934384818041040558738047938191128837513641312073228
n = 60963366078211892139782164553229839791502084065797427186542618397545727161274841617686250921963611437080013453945352358942521066741014917856501958079694414085090202899360268239782866048857013018556075611212967681579752043806346865240798665941810915921007045224109588567326403486828349669686252547982832071281
e = 7184034609793405908044885436388514163140982883564300016199530675561067044059471776452857406813326382479651859328622858356548059850784415072489809149785309658703919120574659520867024799474294772496700841351558889505905592710968805928143542091733183171013724562937755877941778591784097846967401066275244391121

def continued_fraction_expansion(x):
    """Compute the continued fraction expansion of x."""
    fractions = []
    while True:
        integer_part = int(x)
        fractions.append(integer_part)
        x -= integer_part
        if x == 0:
            break
        x = 1 / x
    return fractions

def convergents(continued_fraction):
    """Calculate the convergents of the continued fraction."""
    p0, p1 = 0, 1
    q0, q1 = 1, 0
    for a in continued_fraction:
        p = a * p1 + p0
        q = a * q1 + q0
        yield (p, q)
        p0, p1 = p1, p
        q0, q1 = q1, q

def wieners_attack(n, e):
    """Implement Wiener’s attack on RSA."""
    # Compute continued fraction expansion of e/n
    cf = continued_fraction_expansion(Fraction(e, n))
    
    # Generate convergents and test them
    for (k, (p, q)) in enumerate(convergents(cf)):
        # If q is zero, skip
        if q == 0:
            continue
        
        # Calculate d
        try:
            d = inverse(p, q)
            # Verify if d is correct
            if (p * d) % ((p * q) - 1) == 1:
                return d
        except ValueError:
            # If inverse fails, we skip
            continue

    return None

# Perform the attack
d = wieners_attack(n, e)

if d:
    print(f"Found d: {d}")
    # Now decrypt the message
    m = pow(c, d, n)
    print(f"Decrypted message (m): {m}")
else:
    print("Failed to find d.")

