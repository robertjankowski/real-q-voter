package pl.fweis;

import com.mxgraph.layout.mxCircleLayout;
import org.jgrapht.Graph;
import org.jgrapht.ext.JGraphXAdapter;
import org.jgrapht.graph.DefaultDirectedGraph;
import org.jgrapht.graph.DefaultEdge;

import javax.swing.*;

import com.mxgraph.swing.mxGraphComponent;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class Main extends JFrame {

    public Main() {
        Graph<String, DefaultEdge> g = new DefaultDirectedGraph(DefaultEdge.class);
        g.addVertex("a");
        g.addVertex("b");
        g.addVertex("c");
        g.addEdge("a", "b");
        g.addEdge("a", "c");
        g.addEdge("c", "b");

        List<Integer> vertexDistr = new ArrayList<>();
        for (var vertex : g.vertexSet())
            vertexDistr.add(g.degreeOf(vertex));
        vertexDistr.forEach(System.out::println);

        JGraphXAdapter<String, DefaultEdge> graphXAdapter = new JGraphXAdapter<>(g);
        mxGraphComponent component = new mxGraphComponent(graphXAdapter);
        component.setConnectable(false);
        component.getGraph().setAllowDanglingEdges(false);
        getContentPane().add(component);

        mxCircleLayout layout = new mxCircleLayout(graphXAdapter);
        // center the circle
        int radius = 100;
        Dimension DEFAULT_SIZE = new Dimension(530, 320);
        layout.setX0((DEFAULT_SIZE.width / 2.0) - radius);
        layout.setY0((DEFAULT_SIZE.height / 2.0) - radius);
        layout.setRadius(radius);
        layout.setMoveCircle(true);
        layout.setDisableEdgeStyle(true);

        layout.execute(graphXAdapter.getDefaultParent());
    }

    public static void main(String[] args) {
        Main main = new Main();
        main.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        main.pack();
        main.setSize(400, 400);
        main.setVisible(true);
    }
}
