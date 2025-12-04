#!/usr/bin/env bb

(require '[clojure
           [string :as str]
           set
           [pprint :refer [pprint]]]
  '[clojure.math.numeric-tower :as math])

(def rx #"(\w{3})\s=\s\((\w{3}),\s(\w{3})\)")
(defn read-data [fname]
  (let [[commands _ & raw-map] (-> fname
                                 slurp
                                 (str/split #"\n"))
        map (reduce (fn [acc l]
                      (let [[_ a b c] (re-matches rx l)]
                           (assoc acc a [b c]))) {} raw-map)]
    [commands map]))

;; 1
(let [[commands m] (read-data "in/8.txt")]
  (loop [steps (map vector (cycle commands) (range))
         pos   "AAA"]
    (let [[cmd c]  (first steps)
          [L R]    (get m pos)
          next-pos (if (= cmd \L) L R)]
      (if (= next-pos "ZZZ")
        (inc c)
        (recur (rest steps) next-pos)))))
;; 20569

;; 2

;; all cycles are stable.
(let [[commands m] (read-data "in/8.txt")
      starts       (->> (keys m) (filter #(str/ends-with? % "A")))
      lengths      (for [s starts]
                     (loop [steps (map vector (cycle commands) (range))
                            pos   s]
                       (let [[cmd c]  (first steps)
                             [L R]    (get m pos)
                             next-pos (if (= cmd \L) L R)]
                    (if (str/ends-with? next-pos "Z")
                      (inc c)
                      (recur (rest steps) next-pos)))))]
  (reduce math/lcm lengths))
