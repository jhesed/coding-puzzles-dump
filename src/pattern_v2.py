G = {
    "A": set("BED"),
    "B": set("CFEDA"),
    "C": set("FEB"),
    "D": set("ABEHG"),
    "E": set("BCFIHGDA"),
    "F": set("CIHEB"),
    "G": set("DEH"),
    "H": set("EFIGD"),
    "I": set("FHE"),
}

result = 0


def count_patterns_from(node, length, list):
    if length == 1:
        print(G[node])
        return len(G[node])
    global result
    for neighbor in G[node]:
        if neighbor not in list:
            result += count_patterns_from(
                neighbor, length - 1, list.append(neighbor)
            )
    return result


if __name__ == "__main__":
    # print("A: ---------------", get_neighbors("A"))
    # print("B: ---------------", get_neighbors("B"))
    # print("C: ---------------", get_neighbors("C"))
    # print("D: ---------------", get_neighbors("D"))

    print("C: ---------------", count_patterns_from("C", length=2, list=[]))
